# responsible to maintain business rules for important decisions between routes and repositories
# the service doesn't do directly operations on DB, these responsabilities are send to repositories
from sqlalchemy.orm import Session
from models.product import Product
from repositories import product_repository
from schemas.product import ProductCreate, ProductUpdate 

def create_product(db: Session, data: ProductCreate):
    availability = data.stock > 0

    product = Product(
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock,
        availability=availability
    )

    return product_repository.create(db, product)

def update_product(db: Session, product: Product, data: ProductUpdate):
    updated_data = data.models_dump(exclude_unset=True)

    if "stock" in updated_data:
        updated_data["availability"] = updated_data["stock"] > 0

    return product_repository.update(db, product, updated_data)