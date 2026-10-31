from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Synthetic API Integration")
ORDERS = {"ORD-101": {"customer":"Sample Customer","amount_cents":4995,"status":"ready"}, "ORD-102":{"customer":"Demo Buyer","amount_cents":1900,"status":"pending"}}

class SyncRequest(BaseModel):
    order_id: str = Field(min_length=1, max_length=40)

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!doctype html><html lang="en"><meta charset="utf-8"><title>API Integration Demo</title><h1>Order Integration</h1><p>Synthetic data only</p><label for="order">Order</label><select id="order"><option>ORD-101</option><option>ORD-102</option></select><button onclick="sync()">Sync</button><pre id="result" aria-live="polite"></pre><script>async function sync(){let r=await fetch('/sync',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({order_id:document.getElementById('order').value})});document.getElementById('result').textContent=JSON.stringify(await r.json(),null,2)}</script></html>"""

@app.get("/orders")
def orders():
    return {"orders": sorted(ORDERS)}

@app.post("/sync")
def sync(request: SyncRequest):
    order = ORDERS.get(request.order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"result":"validated","payload":{"external_id":request.order_id,"customer_name":order["customer"],"total_cents":order["amount_cents"],"fulfilment_state":order["status"]}}
