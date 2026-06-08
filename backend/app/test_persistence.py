import asyncio
import inspect

from dotenv import load_dotenv

load_dotenv()

from persistence_kit.repository_factory.factory.repository_factory import (
    get_repo,
    set_registry_initializer
)

from persistence_kit.settings.repo_settings import RepoSettings

from app.persistence.entity_registry import register_entities
from app.entities.product_entity import ProductEntity


async def main():
    set_registry_initializer(register_entities)

    repo = get_repo("product")

    print(inspect.signature(repo.delete))

asyncio.run(main())