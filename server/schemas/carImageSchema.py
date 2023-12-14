from pydantic import BaseModel, Field
from typing import Optional

# // CREATE TABLE carImg(
# // 	imgID INT AUTO_INCREMENT,
# //     carID INT NOT NULL,
# //     ImageURL varchar(500) NOT NULL,
# //     CONSTRAINT `PK_imgID` PRIMARY KEY (imgID),
# //     CONSTRAINT `FK_carID` FOREIGN KEY (carID) REFERENCES car(carID)
# // );

class CarImg(BaseModel):
  imgID: Optional[int] = Field(None)
  carID: int
  ImageURL: str = Field(max_length=500)
