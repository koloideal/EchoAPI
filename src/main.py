import asyncio
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.database.dao.initialize import InitializeDatabaseInteractor
from src.database.connector import PGConnector
from src.utils.get_config import GetConfig
from src.database.dao.users_dao import UsersDAO

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth2/token")

database_config: dict = GetConfig().get_database_config()


@app.post('/oauth2/token')
async def check_is_auth(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + 'case'}

@app.get("/search/")
async def search_view(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


async def main():
    await InitializeDatabaseInteractor(PGConnector(database=None, **database_config))()
    await UsersDAO(PGConnector(**database_config)).create_user('kolo', 'secret')
    print(await UsersDAO(PGConnector(**database_config)).get_user('kolo'))


asyncio.run(main())

