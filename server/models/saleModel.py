from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String

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

class Sale(Base):
  __tablename__ = "sale"

  saleID = Column(Integer, primary_key=True, autoincrement=True)
  carID = Column(Integer, ForeignKey("car.carID"), nullable=False)
  saleDate = Column(String(10), nullable=False)
  clientID = Column(Integer, ForeignKey("client.clientID"), nullable=False)
  sellerID = Column(Integer, ForeignKey("user.userID"), nullable=False)
  totalPrice = Column(Integer, nullable=False)