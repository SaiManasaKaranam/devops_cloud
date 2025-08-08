from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/goodbye")
def goodbye():
    return {"message": "Goodbye, see you soon!"}

@app.get("/favicon.png")
def favicon():
    return FileResponse("images/favicon.png")
