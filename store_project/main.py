from fastapi import FastAPI, HTTPException
from typing import Any
from scalar_fastapi import get_scalar_api_reference
# from app.schema import shipment  # removed because module not found and not used

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

@app.get ("/shipment")
def get_shipment_by_id(id: int) -> dict[str, Any]: 
    if id not in shipments:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    return shipments[id]

@app.post("/items")
def submit_shipment( data: dict) -> dict[str, Any]:
    content= data["content"]
    weight = data["weight"]

#create and assign shipment new id
    new_id = max(shipments.keys()) + 1      
    shipments[new_id] = data
    return {"id": new_id, "data": data}
@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API ",
    )
@app.get("/shipment/{field}")
def get_shipment_by_field(type: str, value: str) -> dict[str, Any]:
    for shipment in shipments.values():
        if shipment.get(type) == value:
            return shipment
    raise HTTPException(status_code=404, detail="Shipment not found")
@app.put("/shipment")
def shipment_update(id:int, product_no: int, type: str, item:str)-> dict[str, Any]:
    shipments[id] ={
        "product no": product_no,
        "type": type,
        "item": item
    }
    return shipments[id]


@app.patch("/shipment")
def patch_shipment(id:int, product_no: int = None, type: str = None, item:str = None)-> dict[str, Any]:
    shipment = shipments[id]
    # Update only the provided fields
    if product_no:
        shipment["product no"] = product_no
    if type:
        shipment["type"] = type
    if item:
        shipment["item"] = item
    shipments[id] = shipment
    return shipment
@app.delete("/shipment")
def delete_shipment(id: int) ->dict[str, Any]:
    shipments.pop(id)
    return {"message": f"Shipment with id {id} has been deleted"}