import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"text": "Hello World!!!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"text": f"Hello {name}!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
