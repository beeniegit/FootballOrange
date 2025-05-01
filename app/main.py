from fastapi import FastAPI
from api import main

app = FastAPI(
    title="FootballApp",
    description="Demo FastAPI Application",
    openapi_url="/openapi.json"
)


app.include_router(main.api_router)

# Application 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8090)