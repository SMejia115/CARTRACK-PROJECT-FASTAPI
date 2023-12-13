from config.database import Base
from sqlalchemy import Column, Integer, String, Enum, Boolean


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

class User(Base):
  __tablename__ = "user"

  userID = Column(Integer, primary_key=True, autoincrement=True)
  userName = Column(String(25), nullable=False)
  password = Column(String(100), nullable=False)
  identificationNumber = Column(String(30), nullable=False)
  firstName = Column(String(25), nullable=False)
  secondName = Column(String(25))
  lastName = Column(String(25), nullable=False)
  address = Column(String(100), nullable=False)
  phone = Column(String(20), nullable=False)
  role = Column(Enum('seller', 'admin'), nullable=False)
  state = Column(Boolean, nullable=False, default=True)