# Responsible for validate and padronize the data that go in or go out of the API
from pydantic import BaseModel, Field
# pydantic is a high-performance Python data validation and settings management that uses Python type hints
# BaseModel is used for data validation on interface, parsing and serialization based on Python type hints
# Field is used within a BaseModel to apply validation, constraint and metadata
from typing import Optional
from decimal import Decimal
# allows the use of type hints to indicate that a variable, function argumente or return value can be None

class ProductBase(BaseModel):
    name:str
    description: str
    price: Decimal = Field(gt=0, description="gt=0: the price product will always be bigger then zero") 
    stock: int = Field(ge=0, description="ge=0: the price product will never  be less than zero") 

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[Decimal] = Field(gt=0)
    stock: Optional[int] = Field(ge=0)

class ProductResponse(ProductBase):
    id: int
    availability: bool

    class Config:
        from_attributes = True # Allow fastAPI converts automatically ORM objects in JSON responses, this