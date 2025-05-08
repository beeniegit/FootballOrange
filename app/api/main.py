from fastapi import APIRouter
from api.routes import route, routeDB, routeQuery

api_router = APIRouter()

# api_router.include_router(route.router)
# api_router.include_router(routeDB.router)
api_router.include_router(routeQuery.router)