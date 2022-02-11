from fastapi import FastAPI, applications
from app.handlers import router



def get_application() -> FastAPI:
    applications = FastAPI()
    applications.include_router(router)
    return applications

app = get_application()

