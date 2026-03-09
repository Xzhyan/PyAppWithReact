from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def register_middleware(app: FastAPI):
    origins = [
        'http://localhost:5173',
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )