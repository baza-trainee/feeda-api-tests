from pydantic import BaseModel, Field


class TypeProject(BaseModel):
    project_type: str = Field(..., max_length=15, min_length=1)
