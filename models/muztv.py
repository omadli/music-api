from pydantic import BaseModel
from typing import Optional

class Query(BaseModel):
    """Request query"""
    query: str
    page: Optional[int] = 1

    class Config:
        schema_extra = {
            "example": {
                "query": "Doxxim",
                "page" : 1
            }
        }