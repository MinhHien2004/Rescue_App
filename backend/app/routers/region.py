from fastapi import APIRouter

router = APIRouter(prefix="/region", tags=["region"])

@router.get("/")
def get_region():
    return "đây là router region"
