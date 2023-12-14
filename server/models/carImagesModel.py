from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String

# // CREATE TABLE carImg(
# // 	imgID INT AUTO_INCREMENT,
# //     carID INT NOT NULL,
# //     ImageURL varchar(500) NOT NULL,
# //     CONSTRAINT `PK_imgID` PRIMARY KEY (imgID),
# //     CONSTRAINT `FK_carID` FOREIGN KEY (carID) REFERENCES car(carID)
# // );

class CarImg(Base):
  __tablename__ = "carImg"

  imgID = Column(Integer, primary_key=True, autoincrement=True)
  carID = Column(Integer, ForeignKey("car.carID"), nullable=False)
  imageURL = Column(String(500), nullable=False)

 