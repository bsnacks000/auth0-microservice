
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routes import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*", # XXX need to fix this boi
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(user_router)