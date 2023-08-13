from pydantic import BaseModel
from datetime import date
from typing import Optional

from models.user_project.type_project import TypeProjectResponse
from models.user_project.status_project import StatusProjectResponse
from models.user_project.complexity import ComplexityResponse


class ProjectsResponse(BaseModel):
    id: Optional[int] = None  # readOnly
    title: str
    type_project: TypeProjectResponse
    project_status: StatusProjectResponse
    start_date_project: date
    complexity: ComplexityResponse
    participants_count: Optional[str] = None  # readOnly

    class Config:
        min_properties = 5
