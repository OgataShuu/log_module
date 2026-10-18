from fastapi import FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from router import user

app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}

app.include_router(user.router)