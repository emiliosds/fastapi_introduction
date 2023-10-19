from fastapi import FastAPI, APIRouter
from views import user_router, assets_router
from views_sync import sync_router
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
main_router = APIRouter()

app.mount("/static", StaticFiles(directory="static"), name="static")

@main_router.get('/')
async def main():
    return FileResponse('static/index.html')

app.include_router(router=main_router)
app.include_router(user_router)
app.include_router(assets_router)
app.include_router(sync_router)