from pydantic import BaseModel


class LogoutSuccess(BaseModel):
    pass


class LogoutError(BaseModel):
    message: str
