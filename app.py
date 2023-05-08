from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://tap-gui.tap.tanzu.dk",
    "https://tap-gui.tap.tanzu.dk",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "Hello World from FastAPI Accelerator with Auto API registration!!!"
    }


@app.get("/api1")
async def devopsconf1():
    return {"message": "Hello World from api 1"}


@app.get("/api2")
async def devopsconf2():
    return {"message": "Hello World from api 2"}
