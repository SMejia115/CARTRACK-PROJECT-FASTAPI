from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Database
from config.database import Session

# Schemas
from schemas.userSchema import User

# Models
from models.userModel import User as UserModel

from fastapi.encoders import jsonable_encoder


usersRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
#Create User
@usersRouter.post("/users", tags=["users"])
def createUser(user: User):
  db = Session()
  newUser = UserModel(**user.model_dump())
  db.add(newUser)
  db.commit()
  return JSONResponse(status_code=201, content={"message": "User created successfully"})



#------------------------------------------- G E T ----------------------------------------------
#------------------------------------------------------------------------------------------------
#Get all users
@usersRouter.get("/users", tags=["users"])
def getAllUsers():
  db = Session()
  users = db.query(UserModel).all()
  return JSONResponse(status_code=200, content=jsonable_encoder(users))

#------------------------------------------------------------------------------------------------
#Get user by ID
@usersRouter.get("/users/{userID}", tags=["users"])
def getUserByID(userID: int):
  db = Session()
  user = db.query(UserModel).filter(UserModel.userID == userID).first()
  return JSONResponse(status_code=200, content=jsonable_encoder(user))

#------------------------------------------------------------------------------------------------
#Get user by username
@usersRouter.get("/users/username/{username}", tags=["users"])
def getUserByUsername(username: str):
  db = Session()
  user = db.query(UserModel).filter(UserModel.userName == username).first()
  return JSONResponse(status_code=200, content=jsonable_encoder(user))




#------------------------------------------ P U T -----------------------------------------------
#------------------------------------------------------------------------------------------------
#Update user by ID
@usersRouter.put("/users/{userID}", tags=["users"])
def updateUserByID(userID: int, user: User):
  db = Session()
  user = db.query(UserModel).filter(UserModel.userID == userID).update(user.model_dump())
  db.commit()
  return JSONResponse(status_code=200, content={"message": "User updated successfully"})