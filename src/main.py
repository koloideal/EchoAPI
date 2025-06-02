from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.database.dao.initialize import InitializeDatabaseDAO

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post('/oauth2/token')
async def check_is_auth(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + 'case'}

@app.get("/search/")
async def search_view(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}