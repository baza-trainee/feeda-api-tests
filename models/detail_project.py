from pydantic import BaseModel, Field
from typing import Optional

from models.complexity import ComplexityModel
from models.status_project import StatusProjectModel
from models.type_project import TypeProjectModel


class DetailProjectModel(BaseModel):
    id: Optional[int]
    type_project: TypeProjectModel
    complexity: ComplexityModel
    project_status: StatusProjectModel
    title: str = Field(..., max_length=50, min_length=1)
    comment: Optional[str] = Field(None, max_length=50)
    start_date_project: str  # Assuming the format is a string representing a date
    end_date_project: Optional[str] = None  # Assuming the format is a string representing a date
    address_site: Optional[str] = None  # Assuming the format is a URI string
    url: str = Field(..., regex=r'^[-a-zA-Z0-9_]+$', max_length=30, min_length=1)
