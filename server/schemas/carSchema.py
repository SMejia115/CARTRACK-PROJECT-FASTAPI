from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import date

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


class Car(BaseModel):
  carID: Optional[int] = Field(None)
  brand: str = Field(max_length=30)
  model: str = Field(max_length=30)
  year: str = Field(max_length=4)
  color: str = Field(max_length=20)
  fuelType: str = Field(max_length=20)
  chassisNumber: str = Field(max_length=30)
  engineNumber: str = Field(max_length=30)
  licensePlate: str = Field(max_length=7)
  city: str = Field(max_length=25)
  appraisal: int
  cylinderCapacity: str = Field(max_length=25)
  transitLicenseNumber: str = Field(max_length=30)
  soatDate: date
  tecnoDate: date
  previousOwner: Optional[int] = Field(None)
  type: str = Field(max_length=20)
  status: str = Field(max_length=20)

