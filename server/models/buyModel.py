from config.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey

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

class Buy(Base):
  __tablename__ = "buy"

  buyID = Column(Integer, primary_key=True, autoincrement=True)
  buyDate = Column(Date, nullable=False)
  sellerID = Column(Integer, ForeignKey("client.clientID"), nullable=False)
  buyerID = Column(Integer, ForeignKey("user.userID"), nullable=False)
  carID = Column(Integer, ForeignKey("car.carID"), nullable=False)
  
