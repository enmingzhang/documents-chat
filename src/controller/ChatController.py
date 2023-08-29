from fastapi import APIRouter

router = APIRouter()


@router.get("/chat")
def read_root():
    return {"hi": "openai"}
