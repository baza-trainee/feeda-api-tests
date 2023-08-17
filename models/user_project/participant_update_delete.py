from pydantic import BaseModel, Field
from typing import Optional
from typing import List


class ParticipantUpdateDeleteResponse(BaseModel):
    id: str = Field(..., max_length=36)  # Assuming the format is a UUID string
    first_name: str = Field(..., max_length=20, min_length=1)
    last_name: str = Field(..., max_length=50, min_length=1)
    comment: Optional[str] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=128)
    email: str = Field(..., max_length=70, min_length=1)
    account_discord: str = Field(..., max_length=37, min_length=1)
    account_linkedin: str = Field(..., max_length=128, min_length=1)
    city: str = Field(..., max_length=50, min_length=1)
    experience: bool
    stack: Optional[str] = Field(None, max_length=300)
    speciality: Optional[int] = None
    project: Optional[List[int]] = None
    type_participant: Optional[int] = None
