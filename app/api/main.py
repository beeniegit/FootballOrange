from fastapi import APIRouter
from api.routes import route

api_router = APIRouter()

api_router.include_router(route.router)
