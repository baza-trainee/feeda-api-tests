from pydantic import BaseModel, Field


class StatusProjectResponse(BaseModel):
    status: str = Field(..., max_length=20, min_length=1)
