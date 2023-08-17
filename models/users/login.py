from pydantic import BaseModel, field_validator


class LoginSuccessResponse(BaseModel):
    token: str


class LoginErrorResponse(BaseModel):
    message: str

    @field_validator('message')
    def check_message(cls, value):
        if value != "Invalid data":
            raise ValueError(f"Incorrect value: {value}")

        return value
