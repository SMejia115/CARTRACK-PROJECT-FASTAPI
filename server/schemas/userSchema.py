from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

# // CREATE TABLE user(
# // 	userID INT AUTO_INCREMENT,
# //     userName VARCHAR(25) NOT NULL,
# //     password VARCHAR(100) NOT NULL,
# //     identificationNumber VARCHAR(30) NOT NULL,
# //     firstName VARCHAR(25) NOT NULL,
# //     secondName VARCHAR(25),
# //     lastName VARCHAR(25) NOT NULL,
# //     address TEXT NOT NULL,
# //     phone VARCHAR(20) NOT NULL,
# //     role ENUM('seller', 'admin') NOT NULL,
# //     state BIT DEFAULT 1 NOT NULL,
# //     CONSTRAINT `PK_userID` PRIMARY KEY (userID)
# // );

class UserRole(str, Enum):
    seller = 'seller'
    admin = 'admin'

class User(BaseModel):
  userID: Optional[int] = Field(None)
  userName: str = Field(max_length=25)
  password: str = Field(max_length=100)
  identificationNumber: str = Field(max_length=30)
  firstName: str = Field(max_length=25)
  secondName: Optional[str] = Field(max_length=25)
  lastName: str = Field(max_length=25)
  address: str = Field(max_length=100)
  phone: str = Field(max_length=20)
  role: UserRole
  state: int = Field(default=1)