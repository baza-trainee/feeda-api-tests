from pydantic import BaseModel, Field


class StatusProjectModel(BaseModel):
    status: str = Field(..., max_length=20, min_length=1)
