from pydantic import BaseModel, Field
from typing import Optional

from models.complexity import Complexity
from models.status_project import StatusProject
from models.type_project import TypeProject


class DetailProject(BaseModel):
    id: Optional[int]
    type_project: TypeProject
    complexity: Complexity
    project_status: StatusProject
    title: str = Field(..., max_length=50, min_length=1)
    comment: Optional[str] = Field(None, max_length=50)
    start_date_project: str  # Assuming the format is a string representing a date
    end_date_project: Optional[str] = None  # Assuming the format is a string representing a date
    address_site: Optional[str] = None  # Assuming the format is a URI string
    url: str = Field(..., regex=r'^[-a-zA-Z0-9_]+$', max_length=30, min_length=1)
