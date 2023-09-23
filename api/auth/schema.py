from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    email: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "example@email.com",
            }
        }
