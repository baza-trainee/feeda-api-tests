from pydantic import BaseModel, field_validator


class LogoutSuccess(BaseModel):
    message: str

    @field_validator('message')
    def check_message(cls, value):
        if value != "Delete":
            raise ValueError(f"Incorrect value: {value}")

        return value
