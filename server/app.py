from fastapi import FastAPI
from fastapi.responses import JSONResponse

#Middlewares
from fastapi.middleware.cors import CORSMiddleware


#Models
from models.userModel import User
from models.clientModel import Client
from models.carModel import Car
from models.carImagesModel import CarImg
from models.buyModel import Buy
from models.saleModel import Sale


# Routers
from routes.loginRoutes import loginRouter
from routes.usersRoutes import usersRouter

#DB
from config.database import engine, Base


origins = [
    "http://localhost:4200",  # Puerto en el que va a estar el frontend
]



app = FastAPI()
app.tittle = "CARTRACK - SERVER"
app.version = "1.0.0"

# Middlewares
app.add_middleware(
  CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
  )

# Create DB
Base.metadata.create_all(bind=engine)


app.include_router(loginRouter)
app.include_router(usersRouter)
#----------------------------------------
@app.get("/")
def message():
  return JSONResponse(
    content={
    "message": "Welcome to the CARTRACK - SERVER API",
    'login':{
      'login': 'POST /api/login',
            },
    'users':{
      'createUser': 'POST /users',
      'allUsers': 'GET /users', 
      'userByID': 'GET /users/:userID',
      'userByUsername': 'GET /users/username/:username',
      
      #   'updateUser': 'PUT /api/users/:userID', OJO PENDIENTE
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
      # 'orders': {
      #   'allOrders': 'GET /api/orders', 
      #   'ordersByUserID': 'GET /api/orders/user/:userID',
      #   'createOrder': 'POST /api/orders',
      #           },
      
               }
      }
      , status_code=200)