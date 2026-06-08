import asyncio
from dotenv import load_dotenv

load_dotenv()

from persistence_kit.repository_factory.factory.repository_factory import (
    get_repo,
    set_registry_initializer
)

from app.persistence.entity_registry import register_entities
from app.entities.product_entity import ProductEntity


async def main():
    set_registry_initializer(register_entities)

    repo = get_repo("product")

    entity = ProductEntity(
        nombre="Prueba",
        precio=10,
        image_url="test"
    )

    print(entity)
    print(vars(entity))


asyncio.run(main())