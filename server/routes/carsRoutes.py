from fastapi import APIRouter, HTTPException

from config.database import Session

from models.carModel import Car as CarModel
from models.carImagesModel import CarImg as CarImgModel

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

from schemas.carSchema import Car

carsRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
#Create Car

@carsRouter.post("/cars", tags=["cars"])
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

#------------------------------------------------------------------------------------------------
# Get available cars with her images
@carsRouter.get("/available/cars/images", tags=["cars"])
def getAvailableCarsWithImages():
  db = Session()
  try:
    cars = db.query(CarModel).filter(CarModel.status == "available").all()
    
    carsWithImages = []
    carsWithImages = []
    for car in cars:
      carImages = db.query(CarImgModel).filter(CarImgModel.carID == car.carID).all()
      carImages = [{"ImageURL": image['imageURL']} for image in jsonable_encoder(carImages)]
      car = jsonable_encoder(car)
      car['carImages'] = carImages
      carsWithImages.append(car)
    if not carsWithImages:
      raise HTTPException(status_code=404, detail="No cars found")

    return JSONResponse(status_code=200, content=carsWithImages)
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})

#------------------------------------------------------------------------------------------------
# Get car with images by id
@carsRouter.get("/car/images/{carID}", tags=["cars"])
def getCarWithImagesByID(carID: int):
  db = Session()
  try:
    car = db.query(CarModel).filter(CarModel.carID == carID).first()

    if car is None:
      raise HTTPException(status_code=404, detail="Car not found")

    car_images = db.query(CarImgModel).filter(CarImgModel.carID == car.carID).all()

    car_images = [{"ImageURL": image.imageURL} for image in car_images]
    car_data = jsonable_encoder(car)
    car_data['carImages'] = car_images

    return JSONResponse(status_code=200, content={"car": car_data, "carImages": car_images})
  
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})



#------------------------------------------ P U T -----------------------------------------------
#------------------------------------------------------------------------------------------------
# Update car by ID
@carsRouter.put("/modify/cars/{carID}", tags=["cars"])
def updateCar(carID: int, car: Car):
  db = Session()
  try:
    carToUpdate = db.query(CarModel).filter(CarModel.carID == carID).first()
    if carToUpdate is None:
      raise HTTPException(status_code=404, detail="Car not found")
    carToUpdate.brand = car.brand
    carToUpdate.model = car.model
    carToUpdate.year = car.year
    carToUpdate.color = car.color
    carToUpdate.fuelType = car.fuelType
    carToUpdate.chassisNumber = car.chassisNumber
    carToUpdate.engineNumber = car.engineNumber
    carToUpdate.licensePlate = car.licensePlate
    carToUpdate.city = car.city
    carToUpdate.appraisal = car.appraisal
    carToUpdate.cylinderCapacity = car.cylinderCapacity
    carToUpdate.transitLicenseNumber = car.transitLicenseNumber
    carToUpdate.soatDate = car.soatDate
    carToUpdate.tecnoDate = car.tecnoDate
    carToUpdate.previousOwner = car.previousOwner
    carToUpdate.type = car.type
    carToUpdate.status = car.status
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Car updated successfully"})
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})


#----------------------------------------- D E L E T E ------------------------------------------
#------------------------------------------------------------------------------------------------
