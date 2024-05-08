from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getHello():
    return "hello"