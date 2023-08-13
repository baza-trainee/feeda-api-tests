from pydantic import BaseModel
from typing import Optional

from models.user_project.speciality import SpecialityResponse
from models.user_project.projects import ProjectsResponse
from models.user_project.type_participant import TypeParticipantResponse


class AllParticipantsResponse(BaseModel):
    id: Optional[str] = None  # format: uuid, readOnly
    speciality: SpecialityResponse
    project: ProjectsResponse
    type_participant: TypeParticipantResponse
    first_name: str
    last_name: str
    comment: Optional[str] = None
    phone_number: Optional[str] = None
    email: str
    account_discord: str
    account_linkedin: str
    city: str
    experience: bool
    stack: Optional[str] = None
    conditions_participation: bool
    processing_personal_data: bool

    class Config:
        schema_extra = {
            "first_name": {"minLength": 1, "maxLength": 20},
            "last_name": {"minLength": 1, "maxLength": 50},
            "comment": {"maxLength": 50},
            "phone_number": {"maxLength": 128},
            "email": {"format": "email", "minLength": 1, "maxLength": 70},
            "account_discord": {"minLength": 1, "maxLength": 37},
            "account_linkedin": {"minLength": 1, "maxLength": 128},
            "city": {"minLength": 1, "maxLength": 50},
            "stack": {"maxLength": 300},
        }
