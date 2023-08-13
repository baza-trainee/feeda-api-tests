from pydantic import BaseModel
from typing import List

from models.user_project.projects import ProjectsResponse


class CreateProjectParticipantsResponse(BaseModel):
    id: int
    user: List[str]
    project: ProjectsResponse
