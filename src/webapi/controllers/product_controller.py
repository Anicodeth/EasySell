from typing import Dict, List

from bson import ObjectId
from fastapi import APIRouter, Body, Path

from src.application.use_cases.dtos.product.create_product_dto import \
    CreateProductDto
from src.application.use_cases.dtos.product.product_dto import ProductDto
from src.application.use_cases.services.product_service import ProductService
from src.persistence.db_client import DbClient
from src.persistence.repositories.product_repository import ProductRepository
from src.webapi.responses.api_response import GenericResponse
from src.webapi.schemas.product_schema import ProductCreate

db_client = DbClient()
product_repository = ProductRepository(db_client)
product_service = ProductService(product_repository)

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def list_products() -> GenericResponse[List[ProductDto]]:
    response = product_service.get_all()

    if response.is_success:
        return GenericResponse[List[ProductDto]](
            success=True,
            value=list(map(ProductDto.to_dict, response.value)),
            message="Products retrieved successfully",
        )
    return GenericResponse[List[ProductDto]](
        success=False, value=None, message=response.error
    )


@product_router.post("/")
def create_product(product_data: ProductCreate) -> GenericResponse[dict]:
    product = CreateProductDto(**product_data.dict())
    response = product_service.create(product)

    if response.is_success:
        return GenericResponse[Dict](
            success=True,
            value={"id": str(response.value)},
            message="Product created successfully",
        )

    return GenericResponse[Dict](success=False, value={}, message=response.error)


@product_router.get("/{product_id}")
def get_product(
    product_id: str = Path(..., title="The product ID")
) -> GenericResponse[ProductDto]:
    response = product_service.get(ObjectId(product_id))

    if response.is_success:
        return GenericResponse[ProductDto](
            success=True,
            value=response.value.to_dict(),
            message="Product retrieved successfully",
        )
    return GenericResponse[ProductDto](
        success=False, value=None, message=response.error
    )


@product_router.put("/{product_id}")
def update_product(
    product_id: str = Path(..., title="The product ID"),
    product_data: ProductCreate = Body(..., title="Updated product data"),
) -> GenericResponse[None]:
    product = CreateProductDto(**product_data.dict())
    response = product_service.update(ObjectId(product_id), product)

    if response.is_success:
        return GenericResponse[None](
            success=True, value=None, message="Product updated successfully"
        )

    return GenericResponse[None](success=False, value=None, message=response.error)


@product_router.delete("/{product_id}")
def delete_product(
    product_id: str = Path(..., title="The product ID")
) -> GenericResponse[None]:
    response = product_service.delete(ObjectId(product_id))

    if response.is_success:
        return GenericResponse[None](
            success=True, value=None, message="Product deleted successfully"
        )

    return GenericResponse[None](success=False, value=None, message=response.error)
