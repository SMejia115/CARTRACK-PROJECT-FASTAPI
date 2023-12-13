from fastapi import FastAPI
from fastapi.responses import JSONResponse

#Models
from models.userModel import User
from models.clientModel import Client
from models.carModel import Car
from models.carImagesModel import CarImg
from models.buyModel import Buy
from models.saleModel import Sale


# Routers
from routes.usersRoutes import usersRouter

#DB
from config.database import engine, Base





app = FastAPI()
app.tittle = "CARTRACK - SERVER"
app.version = "1.0.0"


# Create DB
Base.metadata.create_all(bind=engine)


app.include_router(usersRouter)
#----------------------------------------
@app.get("/")
def message():
  return JSONResponse(
    content={
    "message": "Welcome to the CARTRACK - SERVER API",
    'users': {
      'createUser': 'POST /users',
      'allUsers': 'GET /users', 
      'userByID': 'GET /users/:userID',
      'userByUsername': 'GET /users/username/:username',
      
      #   'updateUser': 'PUT /api/users/:userID',
      #   'deleteUser': 'DELETE /api/users/:userID',
		  # },
      # 'cars': {
      #   'allCars': 'GET /api/products',
      #   'carByID': 'GET /api/products/:productID',
      #   'createCar': 'POST /api/products',
      #   'updateCar': 'PUT /api/products/:productID',
      #   'deleteCar': 'DELETE /api/products/:productID',
      #   },
      # 'images': {
      #   'allImages': 'GET /api/images',
      #   'imageByID': 'GET /api/images/:productID',
      #   'createImage': 'POST /api/images',
      #   'deleteImage': 'DELETE /api/images/:productID',
      #           },
      # 'inventory': {
      #   'allInventory': 'GET /api/inventory',
      #   'inventoryByProductID': 'GET /api/inventory/product/:productID',
      #   'updateInventory': 'PUT /api/inventory/product/:productID',
      #           },
      # 'orders': {
      #   'allOrders': 'GET /api/orders', 
      #   'ordersByUserID': 'GET /api/orders/user/:userID',
      #   'createOrder': 'POST /api/orders',
      #           },
      # 'payment': {
      #   'paymentLinkSuccess': 'POST /api/payment/success',
      #   'paymentLinkCancel': 'POST /api/payment/cancel',
      #           },
      # 'login': {
      #   'login': 'POST /api/login',
               }
      }
      , status_code=200)