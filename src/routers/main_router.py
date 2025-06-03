from fastapi import APIRouter


main_router: APIRouter = APIRouter()

@main_router.get("/search/")
async def search_view():
    return
