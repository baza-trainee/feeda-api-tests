from pydantic import BaseModel
from typing import Optional


class SpecialityResponse(BaseModel):
    id: Optional[int] = None  # readOnly
    title: str

    class Config:
        min_properties = 1
        validate_all = True
