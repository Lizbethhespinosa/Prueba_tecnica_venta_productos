from sqlalchemy import Column, Integer, String, Numeric
from app.config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Numeric, nullable=False)
    image_url = Column(String, nullable=False)