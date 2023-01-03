from pydantic import BaseModel
from typing import Optional

class ProvinciaSchema(BaseModel):
    id: Optional[int]
    name: str
    
