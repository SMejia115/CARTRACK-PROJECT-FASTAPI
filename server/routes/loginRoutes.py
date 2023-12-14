from fastapi import APIRouter

from schemas.loginSchema import Login

from config.database import Session

from models.userModel import User as UserModel

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

from utils.jwt_manager import create_token, decode_token


loginRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
# Validate user

@loginRouter.post("/login", tags=["login"])
def validateUser(login: Login):
  username = login.userName
  password = login.password
  try:
    db = Session()
    user = db.query(UserModel).filter(UserModel.userName == username).first()
    if user.password == password:
      token = create_token(data = {'user':jsonable_encoder(user)})
      print(token)
      return JSONResponse({'token':token}, status_code=200)
    else:
      print("Wrong user")
      return JSONResponse(status_code=404, content={"message": "Wrong user"})
  except Exception as e:
    print("Error: ", e)
    return JSONResponse(status_code=500, content={"message": "Error"})

