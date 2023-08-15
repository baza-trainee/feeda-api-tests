from pydantic import BaseModel


class LogoutError(BaseModel):
    message: str
