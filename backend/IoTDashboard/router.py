from fastapi import APIRouter, Depends

from IoTDashboard.services.jwt import get_auth_user

router = APIRouter()

# Add routers here via router.include_router({router_name})


@router.get("/health")
async def health():
    return {"status": "success"}


@router.get("/test_jwt")
async def test_jwt(user: dict = Depends(get_auth_user)):
    return {"status": "Authentication Passed"}
