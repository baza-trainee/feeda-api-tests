from pydantic import BaseModel
from typing import List

from models.project import ProjectModel


class CreateProjectParticipantsModel(BaseModel):
    id: int
    user: List[str]
    project: ProjectModel
