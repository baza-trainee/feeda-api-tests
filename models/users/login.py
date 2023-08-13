from pydantic import BaseModel


class LoginSuccessResponse(BaseModel):
    token: str


class LoginErrorResponse(BaseModel):
    message: str = "Invalid data provided"
