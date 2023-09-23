from typing import Dict, List

from bson import ObjectId
from fastapi import APIRouter, Body, Path

from src.application.features.product.dtos.create_product_dto import \
    CreateProductDto
from src.application.features.product.dtos.product_dto import ProductDto
from src.application.features.product.product_service import ProductService
from src.persistence.repositories.unit_of_work import UnitOfWork
from src.webapi.responses.api_response import GenericResponse

unit_of_work = UnitOfWork()
product_service = ProductService(unit_of_work)

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.get("/")
def list_products() -> GenericResponse[List[ProductDto]]:
    response = product_service.get_all()

    if response.is_success:
        return GenericResponse[List[ProductDto]](
            success=True,
            value=[product.to_dict() for product in response.value],
            message="Products retrieved successfully.",
        )
    return GenericResponse[List[ProductDto]](
        success=False,
        value=None,
        message="Products list couldn't be retrieved.",
        error=response.error,
    )


@product_router.post("/")
def create_product(product: CreateProductDto) -> GenericResponse[dict]:
    response = product_service.create(product)

    if response.is_success:
        return GenericResponse[Dict](
            success=True,
            value={"id": str(response.value)},
            message="Product created successfully.",
        )

    return GenericResponse[Dict](
        success=False,
        value=None,
        message="Product could not be created.",
        error=response.error,
    )


@product_router.get("/{product_id}")
def get_product(
    product_id: str = Path(..., title="The product ID")
) -> GenericResponse[ProductDto]:
    response = product_service.get(ObjectId(product_id))

    if response.is_success:
        return GenericResponse[ProductDto](
            success=True,
            value=response.value.to_dict(),
            message="Product retrieved successfully.",
        )
    return GenericResponse[ProductDto](
        success=False,
        value=None,
        message="Product could not be retrieved.",
        error=response.error,
    )


@product_router.put("/{product_id}")
def update_product(
    product_id: str = Path(..., title="The product ID"),
    product: CreateProductDto = Body(..., title="Updated product data"),
) -> GenericResponse[None]:
    response = product_service.update(ObjectId(product_id), product)

    if response.is_success:
        return GenericResponse[None](
            success=True, value=None, message="Product updated successfully."
        )

    return GenericResponse[None](
        success=False,
        value=None,
        message="Product could not be updated.",
        error=response.error,
    )


@product_router.delete("/{product_id}")
def delete_product(
    product_id: str = Path(..., title="The product ID")
) -> GenericResponse[None]:
    response = product_service.delete(ObjectId(product_id))

    if response.is_success:
        return GenericResponse[None](
            success=True, value=None, message="Product deleted successfully."
        )

    return GenericResponse[None](
        success=False,
        value=None,
        message="Product could not be deleted.",
        error=response.error,
    )
