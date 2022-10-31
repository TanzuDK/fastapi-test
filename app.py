from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI Accelerator"}

@app.get("/api1")
async def devopsconf1():
    return {"message": "Hello from api 1"}

@app.get("/api2")
async def devopsconf2():
    return {"message": "Hello from api 2"}
