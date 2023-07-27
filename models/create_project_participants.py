from pydantic import BaseModel
from typing import List

from models.project import Project


class CreateProjectParticipants(BaseModel):
    id: int
    user: List[str]
    project: Project
