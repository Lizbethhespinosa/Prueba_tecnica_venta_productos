from fastapi import APIRouter

router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"]
)

@router.get("/")
async def get_purchases():
    return {"message": "Purchases"}