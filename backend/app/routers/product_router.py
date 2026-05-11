from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.product_schema import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)

from app.services.product_service import (
    create_product,
    get_products,
    get_product_by_id,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# CREAR PRODUCTO
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=201
)
def create_new_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    return create_product(db, product)


# OBTENER TODOS
@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_all_products(
    db: Session = Depends(get_db)
):

    return get_products(db)


# OBTENER POR ID
@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = get_product_by_id(
        db,
        product_id
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return product


# ACTUALIZAR
@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_existing_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):

    updated_product = update_product(
        db,
        product_id,
        product_data
    )

    if not updated_product:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return updated_product


# ELIMINAR
@router.delete("/{product_id}")
def delete_existing_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    deleted_product = delete_product(
        db,
        product_id
    )

    if not deleted_product:

        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {
        "message": "Producto eliminado correctamente"
    }