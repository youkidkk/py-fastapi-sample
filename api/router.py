import uvicorn
from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get("/")
async def root():
    return {"text": "Root"}


@router.get("/child")
async def child():
    return {"text": "Child"}


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
