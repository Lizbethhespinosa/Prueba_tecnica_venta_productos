from sqlalchemy.orm import Session

from app.models.purchase_model import Purchase
from app.models.user_model import User
from app.models.product_model import Product

from app.schemas.purchase_schema import (
    PurchaseCreate
)


# CREAR COMPRA
def create_purchase(
    db: Session,
    purchase: PurchaseCreate
):

    # VALIDAR USUARIO
    user = db.query(User).filter(
        User.id == purchase.user_id
    ).first()

    if not user:
        return {
            "error": "Usuario no existe"
        }

    # VALIDAR PRODUCTO
    product = db.query(Product).filter(
        Product.id == purchase.product_id
    ).first()

    if not product:
        return {
            "error": "Producto no existe"
        }

    new_purchase = Purchase(
        user_id=purchase.user_id,
        product_id=purchase.product_id,
        total_productos=purchase.total_productos
    )

    db.add(new_purchase)

    db.commit()

    db.refresh(new_purchase)

    return new_purchase


# OBTENER TODAS
def get_purchases(db: Session):

    return db.query(Purchase).all()


# OBTENER POR ID
def get_purchase_by_id(
    db: Session,
    purchase_id: int
):

    return db.query(Purchase).filter(
        Purchase.id == purchase_id
    ).first()


# ELIMINAR
def delete_purchase(
    db: Session,
    purchase_id: int
):

    purchase = db.query(Purchase).filter(
        Purchase.id == purchase_id
    ).first()

    if not purchase:
        return None

    db.delete(purchase)

    db.commit()

    return purchase