from fastapi import FastAPI
from typing import Any
app = FastAPI()
shipments = {
    110: {"product no": 1100, "type": "furniture", "item": "chair"},
    290: {"product no": 2900, "type": "electronics", "item": "laptop"},
    330: {"product no": 3300, "type": "clothing", "item": "shirt"},
    430: {"product no": 4300, "type": "books", "item": "novel"},
    520: {"product no": 5200, "type": "furniture", "item": "desk"},
    200: {"product no": 2000, "type": "furniture", "item": "chair"}
}

@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

@app.get ("/shipment/{id}")
def get_shipment_by_id(id: int) -> dict[str, Any]: 
    if id not in shipments:
        return {"error": "Shipment not found"}  
    
    return shipments[id]