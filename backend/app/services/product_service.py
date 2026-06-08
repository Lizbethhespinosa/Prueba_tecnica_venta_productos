from persistence_kit.repository_factory.factory.repository_factory import (
    get_repo
)

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate
)

from app.entities.product_entity import ProductEntity

# CREAR PRODUCTO
async def create_product(
    product: ProductCreate
):

    repo = get_repo("product")

    products = await repo.list()

    next_id = max(
        [p.id for p in products],
        default=0
    ) + 1

    new_product = ProductEntity(
        id=next_id,
        nombre=product.nombre,
        precio=float(product.precio),
        image_url=product.image_url
    )

    await repo.add(new_product)

    return new_product

# OBTENER TODOS
async def get_products():

    repo = get_repo("product")

    return await repo.list()


# OBTENER POR ID
async def get_product_by_id(
    product_id: int
):

    repo = get_repo("product")

    return await repo.get(product_id)

# ACTUALIZAR
async def update_product(
    product_id: int,
    product_data: ProductUpdate
):

    repo = get_repo("product")

    product = await repo.get(product_id)

    if not product:
        return None

    product.nombre = product_data.nombre
    product.precio = float(product_data.precio)
    product.image_url = product_data.image_url

    await repo.update(product)

    return product


# ELIMINAR
async def delete_product(
    product_id: int
):

    repo = get_repo("product")

    product = await repo.get(product_id)

    if not product:
        return None

    await repo.delete(product_id)

    return product