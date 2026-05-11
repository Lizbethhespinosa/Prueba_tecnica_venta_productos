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
    create_purchase,
    get_purchases,
    get_purchase_by_id,
    delete_purchase
)

router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"]
)


# CREAR COMPRA
@router.post(
    "/",
    response_model=PurchaseResponse
)
def create_new_purchase(
    purchase: PurchaseCreate,
    db: Session = Depends(get_db)
):

    new_purchase = create_purchase(
        db,
        purchase
    )

    if isinstance(new_purchase, dict):

        raise HTTPException(
            status_code=404,
            detail=new_purchase["error"]
        )

    return new_purchase


# OBTENER TODAS
@router.get(
    "/",
    response_model=list[PurchaseResponse]
)
def get_all_purchases(
    db: Session = Depends(get_db)
):

    return get_purchases(db)


# OBTENER POR ID
@router.get(
    "/{purchase_id}",
    response_model=PurchaseResponse
)
def get_purchase(
    purchase_id: int,
    db: Session = Depends(get_db)
):

    purchase = get_purchase_by_id(
        db,
        purchase_id
    )

    if not purchase:

        raise HTTPException(
            status_code=404,
            detail="Compra no encontrada"
        )

    return purchase


# ELIMINAR
@router.delete("/{purchase_id}")
def delete_existing_purchase(
    purchase_id: int,
    db: Session = Depends(get_db)
):

    deleted_purchase = delete_purchase(
        db,
        purchase_id
    )

    if not deleted_purchase:

        raise HTTPException(
            status_code=404,
            detail="Compra no encontrada"
        )

    return {
        "message": "Compra eliminada correctamente"
    }