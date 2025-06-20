__all__ = (
    "configure_app",
    "create_app",
    "create_async_ioc_container",
)
from collections.abc import Iterable
from contextlib import asynccontextmanager

from dishka import AsyncContainer, Provider, make_async_container, FromDishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from echoapi.database.connector import PGConnector
from echoapi.database.dao.initialize import InitializeDatabaseInteractor
from echoapi.routers.main_router import main_router
from echoapi.routers.security_router import security_router


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI, database_config: FromDishka[dict]):
        await InitializeDatabaseInteractor(PGConnector(database=None, **database_config))()

        yield
    return FastAPI(title=__name__, lifespan=lifespan, default_response_class=ORJSONResponse)


def configure_app(app: FastAPI) -> None:
    app.include_router(main_router)
    app.include_router(security_router)

    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["POST", "OPTIONS"],
        allow_headers=["*"]
    )


def create_async_ioc_container(providers: Iterable[Provider]) -> AsyncContainer:
    return make_async_container(*providers)