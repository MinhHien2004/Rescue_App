from fastapi import APIRouter

router = APIRouter(prefix="/category", tags=["category"])

@router.get("/")
def get_category():
    return "đây là router category"
