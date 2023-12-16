from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import Session

from models.clientModel import Client as ClientModel
from schemas.clientSchema import Client

from fastapi.encoders import jsonable_encoder

clientRouter = APIRouter()

#------------------------------------------ P O S T ---------------------------------------------
#------------------------------------------------------------------------------------------------
#Create Client
@clientRouter.post("/clients", tags=["clients"])
def createClient(client: Client):
  db = Session()
  newClient = ClientModel(**client.model_dump())
  db.add(newClient)
  db.commit()
  return JSONResponse(status_code=201, content={"message": "Client created successfully"})


#------------------------------------------- G E T ----------------------------------------------
#------------------------------------------------------------------------------------------------
# Get all clients
@clientRouter.get("/clients", tags=["clients"])
def getAllClients():
  try:
    db = Session()
    clients = db.query(ClientModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(clients))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})
#------------------------------------------------------------------------------------------------
# Get client by ID
@clientRouter.get("/clients/{clientID}", tags=["clients"])
def getClientByID(clientID: int):
  try:
    db = Session()
    client = db.query(ClientModel).filter(ClientModel.clientID == clientID).first()
    return JSONResponse(status_code=200, content=jsonable_encoder(client))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})

#------------------------------------------------------------------------------------------------
# Get client by identificationNumber
@clientRouter.get("/clients/identificationNumber/{identificationNumber}", tags=["clients"])
def getClientByIdentificationNumber(identificationNumber: str):
  try:
    db = Session()
    client = db.query(ClientModel).filter(ClientModel.identificationNumber == identificationNumber).first()
    if not client:
      return JSONResponse(status_code=404, content={"message": "Client not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(client))
  except Exception as e:
    print(e)
    return JSONResponse(status_code=500, content={"message": "Error"})

#------------------------------------------ P U T -----------------------------------------------
#------------------------------------------------------------------------------------------------



#----------------------------------------- D E L E T E ------------------------------------------
#------------------------------------------------------------------------------------------------
