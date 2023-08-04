from pydantic import BaseModel, Field
from typing import Optional

from models.complexity import ComplexityModel


class ProjectModel(BaseModel):
    id: Optional[int]
    title: str = Field(..., max_length=50, min_length=1)
    start_date_project: str  # Assuming the format is a string representing a date
    complexity: ComplexityModel

    class Config:
        allow_population_by_field_name = True
