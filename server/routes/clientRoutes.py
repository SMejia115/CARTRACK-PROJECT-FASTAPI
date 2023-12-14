from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config.database import Session

from models.clientModel import Client as ClientModel
from schemas.clientSchema import Client

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
 


#------------------------------------------ P U T -----------------------------------------------
#------------------------------------------------------------------------------------------------



#----------------------------------------- D E L E T E ------------------------------------------
#------------------------------------------------------------------------------------------------
