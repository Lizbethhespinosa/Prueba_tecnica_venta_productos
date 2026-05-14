from sqlalchemy.orm import Session

from app.models.purchase_model import Purchase
from app.models.user_model import User
from app.models.product_model import Product

from app.schemas.purchase_schema import PurchaseCreate
from app.config.mongo import purchase_collection


async def create_purchase(
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

    await purchase_collection.insert_one({
        "id": new_purchase.id,
        "user_id": new_purchase.user_id,
        "product_id": new_purchase.product_id,
        "total_productos": new_purchase.total_productos,
        "created_at": new_purchase.created_at
    })

    return new_purchase

