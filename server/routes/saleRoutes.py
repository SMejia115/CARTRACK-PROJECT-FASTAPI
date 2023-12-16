from fastapi import APIRouter

from schemas.saleSchema import Sale

from config.database import Session

from models.saleModel import Sale as SaleModel
from models.carModel import Car as CarModel

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

from sqlalchemy import func


saleRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
# Create a new sale
@saleRouter.post("/sales/add", tags=["sales"])
def createSale(sale: Sale):
  print(sale)
  try:
    db = Session()
    car = db.query(CarModel).filter(CarModel.carID == sale.carID).first()
    if not car:
      return JSONResponse(status_code=404, content={"message": "Car not found"})
    if car.status == "sold":
      return JSONResponse(status_code=404, content={"message": "Car already sold"})
    newSale = SaleModel(**sale.model_dump())
    db.add(newSale)
    car.status = "sold"
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Sale created successfully"})
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})



#------------------------------------------- G E T ----------------------------------------------
#------------------------------------------------------------------------------------------------
# Obtain all sales
@saleRouter.get("/sales", tags=["sales"])
def getAllSales():
  try:
    db = Session()
    sales = db.query(SaleModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(sales))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})

#------------------------------------------------------------------------------------------------
# Obtain all sales by sellerID
@saleRouter.get("/sales/seller/{sellerID}", tags=["sales"])
def getSalesBySellerID(sellerID: int):
  try:
    db = Session()
    sales = db.query(SaleModel).filter(SaleModel.sellerID == sellerID).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(sales))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})

#------------------------------------------------------------------------------------------------
# Calculate the sum of sales by seller
@saleRouter.get("/sales/sum", tags=["sales"])
def get_sum_sales_by_seller():
    try:
        db = Session()
        sales = db.query(SaleModel.sellerID.label("name"),
                         func.sum(SaleModel.totalPrice).label("value")) \
                  .group_by(SaleModel.sellerID) \
                  .all()

        sales_dict = [{"name": sale.name, "value": sale.value} for sale in sales] 

        return JSONResponse(status_code=200, content=sales_dict)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Error"}) 

#------------------------------------------------------------------------------------------------
# Obtain all sales by sellerID
