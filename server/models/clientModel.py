from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String

# // CREATE TABLE Client(
# // 	clientID INT AUTO_INCREMENT,
# //     identificationNumber VARCHAR(30) NOT NULL,
# //     firstName VARCHAR(20) NOT NULL,
# //     secondName VARCHAR(20),
# //     lastName VARCHAR(20) NOT NULL,
# //     address TEXT NOT NULL,
# //     phone VARCHAR(15) NOT NULL,
# //     boolReports BIT DEFAULT 0 NOT NULL,
# //     state BIT DEFAULT 1 NOT NULL,
# //     CONSTRAINT `PK_clientID` PRIMARY KEY (clientID)
# // );

class Client(Base):
  __tablename__ = "client"

  clientID = Column(Integer, primary_key=True, autoincrement=True)
  identificationNumber = Column(String(30), nullable=False)
  firstName = Column(String(20), nullable=False)
  secondName = Column(String(20))
  lastName = Column(String(20), nullable=False)
  address = Column(String(100), nullable=False)
  phone = Column(String(15), nullable=False)
  boolReports = Column(Integer, nullable=False)
  state = Column(Integer, nullable=False)

