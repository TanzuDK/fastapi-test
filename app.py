from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI Accelerator"}

@app.get("/dell")
async def dell():
    return {"message": "Hello World from Dell conf"}
