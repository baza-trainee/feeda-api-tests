from pydantic import BaseModel, Field


class ResetPasswordRequestEmail(BaseModel):
    email: str = Field(..., min_length=2, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
