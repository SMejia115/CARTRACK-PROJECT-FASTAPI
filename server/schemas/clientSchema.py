from pydantic import BaseModel, Field
from typing import Optional


class Client(BaseModel):
  clientID: Optional[int] = Field(None)
  identificationNumber: str = Field(max_length=30)
  firstName: str = Field(max_length=20)
  secondName: Optional[str] = Field(max_length=20)
  lastName: str = Field(max_length=20)
  address: str = Field(max_length=100)
  phone: str = Field(max_length=15)
  state: int = Field(default=1)

