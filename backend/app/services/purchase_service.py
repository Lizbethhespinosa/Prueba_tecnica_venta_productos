from app.schemas.purchase_schema import PurchaseCreate
from app.config.mongo import purchase_collection

from persistence_kit.repository_factory.factory.repository_factory import (
    get_repo
)

from app.entities.purchase_entity import PurchaseEntity


async def create_purchase(
    purchase: PurchaseCreate
):

    user_repo = get_repo("user")
    product_repo = get_repo("product")
    purchase_repo = get_repo("purchase")

    # VALIDAR USUARIO
    user = await user_repo.get(
        purchase.user_id
    )

    if not user:
        return {
            "error": "Usuario no existe"
        }

    # VALIDAR PRODUCTO
    product = await product_repo.get(
        purchase.product_id
    )

    if not product:
        return {
            "error": "Producto no existe"
        }

    purchases = await purchase_repo.list()

    next_id = max(
        [p.id for p in purchases],
        default=0
    ) + 1

    new_purchase = PurchaseEntity(
        id=next_id,
        user_id=purchase.user_id,
        product_id=purchase.product_id,
        total_productos=purchase.total_productos
    )

    await purchase_repo.add(
        new_purchase
    )

    await purchase_collection.insert_one({
        "id": new_purchase.id,
        "user_id": new_purchase.user_id,
        "product_id": new_purchase.product_id,
        "total_productos": new_purchase.total_productos
    })

    return new_purchase