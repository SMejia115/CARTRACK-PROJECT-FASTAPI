from fastapi import APIRouter, File, UploadFile

from config.database import Session

from models.carModel import Car as CarModel

from models.carImagesModel import CarImg as CarImgModel

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

# from config.cloudinary import cloudinary


import cloudinary
# Import the cloudinary.api for managing assets
import cloudinary.api
# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader

cloudinary.config( 
  cloud_name = "duxfb2kob", 
  api_key = "497629393724449", 
  api_secret = "_lqRbVoxrqJKRhh_na526Cutq4M" 
)

import os
# import fs

carsImgRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
#Create Car Image by carID
@carsImgRouter.post("/image/add/{carID}", tags=["carImgs"])
def createCarImg(carID: int, image: UploadFile = File(...)):
  db = Session()
  car = db.query(CarModel).filter(CarModel.carID == carID).first()
  if car is None:
    return JSONResponse(status_code=404, content={"message": "Car not found"})
  else:
    try:
      file_path = f'./uploads/{image.filename}'
      with open(file_path, 'wb') as f:
        f.write(image.file.read())
      upload = cloudinary.uploader.upload(file_path, 
                                          folder='CarTrack/Imgs', 
                                          transformation=[{'width': 800, 'height': 600, 'crop': 'fill'}])
      
      os.remove(file_path)
      imageURL = upload['secure_url']
      newCarImg = CarImgModel(carID=carID, imageURL=imageURL)
      db.add(newCarImg)
      db.commit()
      return JSONResponse(status_code=201, content={"message": "Image created successfully"})
    
    except Exception as e:
      print(e)
      return JSONResponse(status_code=500, content={"message": "Error creating image"})
    
#------------------------------------------------------------------------------------------------
# Create a new car image by licensePlate
@carsImgRouter.post("/image/add/licensePlate/{licensePlate}", tags=["carImgs"])
def createCarImageByLicensePlate(licensePlate: str, image: UploadFile = File(...)):
  db = Session()
  car = db.query(CarModel).filter(CarModel.licensePlate == licensePlate).first()
  if car is None:
    return JSONResponse(status_code=404, content={"message": "Car not found"})
  else:
    try:
      file_path = f'./uploads/{image.filename}'
      with open(file_path, 'wb') as f:
        f.write(image.file.read())
      upload = cloudinary.uploader.upload(file_path, 
                                          folder='CarTrack/Imgs', 
                                          transformation=[{'width': 800, 'height': 600, 'crop': 'fill'}])
      
      os.remove(file_path)
      imageURL = upload['secure_url']
      newCarImg = CarImgModel(carID=car.carID, imageURL=imageURL)
      db.add(newCarImg)
      db.commit()
      return JSONResponse(status_code=201, content={"message": "Image created successfully"})
    
    except Exception as e:
      print(e)
      return JSONResponse(status_code=500, content={"message": "Error creating image"})
#------------------------------------------- G E T ----------------------------------------------
#------------------------------------------------------------------------------------------------
# Get all car images
@carsImgRouter.get("/images", tags=["carImgs"])
def getAllCarImages():
  try:
    db = Session()
    carImages = db.query(CarImgModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(carImages))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})

#------------------------------------------------------------------------------------------------
# Get car image by ID
@carsImgRouter.get("/image/{carImgID}", tags=["carImgs"])
def getCarImageByID(carImgID: int):
  try:
    db = Session()
    carImage = db.query(CarImgModel).filter(CarImgModel.carImgID == carImgID).first()
    return JSONResponse(status_code=200, content=jsonable_encoder(carImage))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})
  
#------------------------------------------------------------------------------------------------
# Get car image by carID
@carsImgRouter.get("/image/car/{carID}", tags=["carImgs"])
def getCarImageByCarID(carID: int):
  try:
    db = Session()
    carImage = db.query(CarImgModel).filter(CarImgModel.carID == carID).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(carImage))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})