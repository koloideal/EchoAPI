import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from echoapi.setup.app_factory import create_async_ioc_container, create_app, configure_app
from echoapi.setup.ioc.registry import get_providers

app: FastAPI = create_app()

configure_app(app=app)
setup_dishka(container=create_async_ioc_container(providers=get_providers()), app=app)


if __name__ == "__main__":
    uvicorn.run(
        app="echoapi.main:app",
        port=8000,
        reload=True,
    )
