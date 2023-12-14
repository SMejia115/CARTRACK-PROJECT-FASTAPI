from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

# // CREATE TABLE sale(
# // 	saleID INT AUTO_INCREMENT,
# //     carID INT NOT NULL,
# //     saleDate DATE NOT NULL,
# //     clientID INT NOT NULL,
# //     sellerID INT NOT NULL,
# //     totalPrice FLOAT NOT NULL,
# //     CONSTRAINT `PK_saleID` PRIMARY KEY (saleID),
# //     CONSTRAINT `FK_carID_sale` FOREIGN KEY (carID) REFERENCES car(carID),
# //     CONSTRAINT `FK_clientID_sale` FOREIGN KEY (clientID) REFERENCES client(clientID),
# //     CONSTRAINT `FK_sellerID_sale` FOREIGN KEY (sellerID) REFERENCES user(userID)
# // );

class Sale(BaseModel):
  saleID: Optional[int] = Field(None)
  carID: int
  saleDate: date
  clientID: int
  sellerID: int
  totalPrice: int

