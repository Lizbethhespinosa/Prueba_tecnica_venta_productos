from sqlalchemy.orm import Session

from app.models.product_model import Product

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate
)


# CREAR PRODUCTO
def create_product(
    db: Session,
    product: ProductCreate
):

    new_product = Product(
        nombre=product.nombre,
        precio=product.precio,
        image_url=product.image_url
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product


# OBTENER TODOS
def get_products(db: Session):

    return db.query(Product).all()


# OBTENER POR ID
def get_product_by_id(
    db: Session,
    product_id: int
):

    return db.query(Product).filter(
        Product.id == product_id
    ).first()


# ACTUALIZAR
def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None

    product.nombre = product_data.nombre
    product.precio = product_data.precio
    product.image_url = product_data.image_url

    db.commit()

    db.refresh(product)

    return product


# ELIMINAR
def delete_product(
    db: Session,
    product_id: int
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return None

    db.delete(product)

    db.commit()

    return product