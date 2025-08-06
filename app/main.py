from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, DevOps World!"}
