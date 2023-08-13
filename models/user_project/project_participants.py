from pydantic import BaseModel
from typing import List, Optional

from models.user_project.projects import ProjectsResponse
from models.user_project.join_user_project import JoinUserProjectResponse


class ProjectParticipantsResponse(BaseModel):
    id: Optional[int] = None  # readOnly
    user: List[JoinUserProjectResponse]
    project: ProjectsResponse
    project_participants: Optional[str] = None  # readOnly

    class Config:
        min_properties = 2
        validate_all = True
