from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def bazar():
    return "hello"

