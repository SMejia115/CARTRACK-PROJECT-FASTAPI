from pydantic import BaseModel, Field

class Login(BaseModel):
  userName: str = Field(max_length=25)
  password: str = Field(max_length=100)