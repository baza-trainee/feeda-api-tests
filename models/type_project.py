from pydantic import BaseModel, Field


class TypeProjectModel(BaseModel):
    project_type: str = Field(..., max_length=15, min_length=1)
