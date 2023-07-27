from pydantic import BaseModel, Field


class Complexity(BaseModel):
    complexity: str = Field(..., max_length=25, min_length=1)
