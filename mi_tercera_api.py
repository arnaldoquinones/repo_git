from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def message():
    return "Dale Boca!!!"


    