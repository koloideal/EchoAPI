from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from src.database.dao.initialize import InitializeDatabaseInteractor
from src.database.connector import PGConnector
from src.utils.get_config import GetConfig
from src.routers.main_router import main_router
from src.routers.security_router import security_router


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth2/token")
database_config: dict = GetConfig().get_database_config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await InitializeDatabaseInteractor(PGConnector(database=None, **database_config))()

    yield


main_app = FastAPI(lifespan=lifespan)

main_app.include_router(main_router)
main_app.include_router(security_router)


