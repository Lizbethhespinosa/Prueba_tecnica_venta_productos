from persistence_kit.repository_factory.registry.entity_registry import (
    register_entity
)

from persistence_kit.settings.constants import Database

from app.entities.product_entity import ProductEntity
from app.entities.user_entity import UserEntity
from app.entities.purchase_entity import PurchaseEntity

def register_entities():

    register_entity(
        "product",
        {
            "entity": ProductEntity,
            "collection": "products",
            "database": Database.POSTGRES
        }

    )

    register_entity(
        "user",
        {
            "entity": UserEntity,
            "collection": "users",
            "database": Database.POSTGRES
        }
    )
    
    register_entity(
        "purchase",
        {
            "entity": PurchaseEntity,
            "collection": "purchases",
            "database": Database.POSTGRES
        }
    )