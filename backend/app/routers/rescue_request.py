from fastapi import APIRouter

router = APIRouter(prefix="/rescue_request", tags=["rescue_request"])

@router.get("/")
def get_rescue_requests():
    return "đây là router rescue_request"
