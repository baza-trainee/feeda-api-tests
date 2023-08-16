from pydantic import BaseModel, Field


class ResetPasswordEmailSuccessResponse(BaseModel):
    email: str = Field(..., min_length=2, pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")


class ResetPasswordEmailErrorResponse(BaseModel):
    message: str
