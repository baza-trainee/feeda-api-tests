from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
import re


class JoinUserProjectResponse(BaseModel):
    id: Optional[UUID] = None  # readOnly
    account_discord: str = re.compile(r"^\w+#\d{4}$")  # Pattern match
    first_name: str
    last_name: str
    phone_number: Optional[str] = None  # x-nullable
    email: EmailStr
    account_linkedin: str
    city: str
    experience: bool
    conditions_participation: bool
    processing_personal_data: bool
    speciality: Optional[int] = None  # x-nullable
    project: Optional[int] = None  # x-nullable
    type_participant: Optional[int] = None  # x-nullable

    class Config:
        min_properties = 6
        validate_all = True
        schema_extra = {
            "patternProperties": {
                "account_discord": {"maxLength": 25, "minLength": 1},
                "first_name": {"maxLength": 20, "minLength": 1},
                "last_name": {"maxLength": 50, "minLength": 1},
                "phone_number": {"maxLength": 128},
                "email": {"maxLength": 70, "minLength": 1},
                "account_linkedin": {"maxLength": 128, "minLength": 1},
                "city": {"maxLength": 50, "minLength": 1},
            }
        }
