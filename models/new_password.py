from pydantic import BaseModel, Field


class NewPasswordModel(BaseModel):
    password: str = Field(..., max_length=12, min_length=8)
    confirm_password: str = Field(..., max_length=12, min_length=8)
    token: str = Field(..., min_length=1)
    uidb64: str = Field(..., min_length=1)
