from pydantic import BaseModel, Field


class TypeProjectResponse(BaseModel):
    project_type: str = Field(..., max_length=15, min_length=1)
