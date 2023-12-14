from fastapi import APIRouter

from config.database import Session

from models.carModel import Car as CarModel

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

from schemas.carSchema import Car

carsRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
#Create Car

@carsRouter.post("/cars/add", tags=["cars"])
def createCar(car: Car):
  db = Session()
  newCar = CarModel(**car.model_dump())
  db.add(newCar)
  db.commit()
  return JSONResponse(status_code=201, content={"message": "Car created successfully"})
  

#------------------------------------------- G E T ----------------------------------------------
#------------------------------------------------------------------------------------------------
#Get all cars
@carsRouter.get("/cars", tags=["cars"])
def getAllCars():
  db = Session()
  cars = db.query(CarModel).all()
  return JSONResponse(status_code=200, content=jsonable_encoder(cars))

#------------------------------------------------------------------------------------------------
#Get car by ID
@carsRouter.get("/cars/{carID}", tags=["cars"])
def getCarByID(carID: int):
  db = Session()
  car = db.query(CarModel).filter(CarModel.carID == carID).first()
  return JSONResponse(status_code=200, content=jsonable_encoder(car))

#------------------------------------------------------------------------------------------------
#Get car by license plate
@carsRouter.get("/cars/licensePlate/{licensePlate}", tags=["cars"])
def getCarByLicensePlate(licensePlate: str):
  db = Session()
  car = db.query(CarModel).filter(CarModel.licensePlate == licensePlate).first()
  return JSONResponse(status_code=200, content=jsonable_encoder(car))

#------------------------------------------------------------------------------------------------
#Get sold cars
@carsRouter.get("/sell/cars", tags=["cars"])
def getSoldCars():
  db = Session()
  cars = db.query(CarModel).filter(CarModel.status == "sold").all()
  return JSONResponse(status_code=200, content=jsonable_encoder(cars))

#------------------------------------------------------------------------------------------------
#Get available cars
@carsRouter.get("/available/cars", tags=["cars"])
def getAvailableCars():
  db = Session()
  cars = db.query(CarModel).filter(CarModel.status == "available").all()
  return JSONResponse(status_code=200, content=jsonable_encoder(cars))




#------------------------------------------ P U T -----------------------------------------------
#------------------------------------------------------------------------------------------------



#----------------------------------------- D E L E T E ------------------------------------------
#------------------------------------------------------------------------------------------------
