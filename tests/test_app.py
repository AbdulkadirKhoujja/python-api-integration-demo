from fastapi.testclient import TestClient
from app import app
client = TestClient(app)

def test_home():
    assert "Order Integration" in client.get("/").text

def test_orders():
    assert client.get("/orders").json()["orders"] == ["ORD-101", "ORD-102"]

def test_sync():
    r = client.post("/sync", json={"order_id":"ORD-101"})
    assert r.status_code == 200
    assert r.json()["payload"]["total_cents"] == 4995

def test_unknown():
    assert client.post("/sync", json={"order_id":"NOPE"}).status_code == 404

def test_invalid():
    assert client.post("/sync", json={"order_id":""}).status_code == 422
