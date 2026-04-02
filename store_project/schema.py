from pydantic import BaseModel,Field
class shipment(BaseModel):
    product_no: int = Field(..., gt=0)
    type: str = Field(..., max_length=100)
    item: str = Field(..., max_length=200)