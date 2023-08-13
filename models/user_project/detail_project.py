from pydantic import BaseModel, Field
from typing import Optional

from models.user_project.complexity import ComplexityResponse
from models.user_project.status_project import StatusProjectResponse
from models.user_project.type_project import TypeProjectResponse


class DetailProjectResponse(BaseModel):
    id: Optional[int]
    type_project: TypeProjectResponse
    complexity: ComplexityResponse
    project_status: StatusProjectResponse
    title: str = Field(..., max_length=50, min_length=1)
    comment: Optional[str] = Field(None, max_length=50)
    start_date_project: str  # Assuming the format is a string representing a date
    end_date_project: Optional[
        str
    ] = None  # Assuming the format is a string representing a date
    address_site: Optional[str] = None  # Assuming the format is a URI string
    url: str = Field(..., regex=r"^[-a-zA-Z0-9_]+$", max_length=30, min_length=1)
