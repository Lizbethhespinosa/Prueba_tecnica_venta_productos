from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.purchase_schema import (
    PurchaseCreate,
    PurchaseResponse
)

from app.services.purchase_service import (
    create_purchase
)

router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"]
)


# ENDPOINT CREAR COMPRA
@router.post(
    "/",
    response_model=PurchaseResponse,
    status_code=201
)
async def create_new_purchase(   # <-- cambio aquí
    purchase: PurchaseCreate,
    db: Session = Depends(get_db)
):

    new_purchase = await create_purchase(   # <-- cambio aquí
        db,
        purchase
    )

    if isinstance(new_purchase, dict):

        raise HTTPException(
            status_code=404,
            detail=new_purchase["error"]
        )

    return new_purchase

