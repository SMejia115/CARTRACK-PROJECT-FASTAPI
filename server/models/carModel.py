from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String

# // CREATE TABLE Car(
# // 	carID INT AUTO_INCREMENT,
# //     brand VARCHAR(30) NOT NULL,
# //     model VARCHAR(30) NOT NULL,
# //     year VARCHAR (4) NOT NULL,
# //     color VARCHAR (20) NOT NULL,
# //     fuelType VARCHAR (20) NOT NULL,
# //     chassisNumber VARCHAR(30) NOT NULL UNIQUE,
# //     engineNumber VARCHAR(30) NOT NULL,
# //     licensePlate VARCHAR(7) NOT NULL UNIQUE,
# //     city VARCHAR(25) NOT NULL,
# //     appraisal FLOAT NOT NULL, 
# //     cylinderCapacity  VARCHAR(25) NOT NULL,
# // 	transitLicenseNumber VARCHAR(30) NOT NULL UNIQUE,
# //     soatDate DATE,
# //     tecnoDate DATE, 
# //     previousOwner INT,
# //     type ENUM('sedan', 'suv', 'pickup', 'hatchback', 'convertible', 'other') NOT NULL,
# //     status ENUM('available', 'sold'),
# //     CONSTRAINT `PK_carID` PRIMARY KEY (carID),
# //     CONSTRAINT `FK_previousOwner` FOREIGN KEY (previousOwner) REFERENCES client(clientID)
# // );

class Car(Base):
  __tablename__ = "car"

  carID = Column(Integer, primary_key=True, autoincrement=True)
  brand = Column(String(30), nullable=False)
  model = Column(String(30), nullable=False)
  year = Column(String(4), nullable=False)
  color = Column(String(20), nullable=False)
  fuelType = Column(String(20), nullable=False)
  chassisNumber = Column(String(30), nullable=False, unique=True)
  engineNumber = Column(String(30), nullable=False)
  licensePlate = Column(String(7), nullable=False, unique=True)
  city = Column(String(25), nullable=False)
  appraisal = Column(Integer, nullable=False)
  cylinderCapacity = Column(String(25), nullable=False)
  transitLicenseNumber = Column(String(30), nullable=False, unique=True)
  soatDate = Column(String(10), nullable=False)
  tecnoDate = Column(String(10), nullable=False)
  previousOwner = Column(Integer, ForeignKey("client.clientID"))
  type = Column(String(20), nullable=False)
  status = Column(String(20), nullable=False)