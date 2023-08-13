from pydantic import BaseModel
from typing import Optional


class TypeParticipantResponse(BaseModel):
    id: Optional[int] = None  # readOnly
    title: str

    class Config:
        schema_extra = {
            "minLength": 1,
            "maxLength": 12,
        }
