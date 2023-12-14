from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# // CREATE TABLE buy(
# // 	buyID INT AUTO_INCREMENT,
# //     buyDate DATE NOT NULL,
# //     sellerID INT NOT NULL, /*Cliente que al que se le compra el carro*/
# //     buyerID INT NOT NULL, /* Vendedor o administrador que recibe el carro */
# //     carID INT NOT NULL,
# //     CONSTRAINT `PK_buyID` PRIMARY KEY (buyID),
# //     CONSTRAINT `FK_sellerID` FOREIGN KEY (sellerID) REFERENCES client(clientID),
# //     CONSTRAINT `FK_buyerID` FOREIGN KEY (buyerID) REFERENCES user(userID),
# //     CONSTRAINT `FK_carID_buy` FOREIGN KEY (carID) REFERENCES car(carID)
# // );

class Buy(BaseModel):
  buyID: Optional[int] = Field(None)
  buyDate: date
  sellerID: int
  buyerID: int
  carID: int