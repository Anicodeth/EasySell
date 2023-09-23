from typing import List

from bson import ObjectId

from src.application.common.responses.base_response import BaseResponse
from src.application.contracts.persistence.product_repository_contract import \
    ProductRepositoryContract
from src.application.use_cases.dtos.product.create_product_dto import \
    CreateProductDto
from src.application.use_cases.dtos.product.product_dto import ProductDto


class ProductService:
    def __init__(self, product_repository: ProductRepositoryContract) -> None:
        self.product_repository: ProductRepositoryContract = product_repository

    def get_all(self) -> BaseResponse[List[ProductDto], str]:
        try:
            products = self.product_repository.list()
            return BaseResponse.success(
                "Products retrieved successfully.",
                list(map(ProductDto.from_entity, products)),
            )
        except Exception:
            return BaseResponse.error(
                "Error retrieving products.", "Internal server error."
            )

    def create(self, product: CreateProductDto) -> BaseResponse[ObjectId, str]:
        try:
            product_id = self.product_repository.add(product.to_entity())
            return BaseResponse.success("Product created successfully.", product_id)
        except Exception:
            return BaseResponse.error(
                "Error creating product.", "Internal server error."
            )

    def get(self, product_id: ObjectId) -> BaseResponse[ProductDto, str]:
        try:
            product = self.product_repository.get(product_id)
            return BaseResponse.success(
                "Product retrieved successfully.", ProductDto.from_entity(product)
            )
        except Exception:
            return BaseResponse.error(
                "Error retrieving product.", "Internal server error."
            )

    def update(
        self, product_id: ObjectId, product: CreateProductDto
    ) -> BaseResponse[None, str]:
        try:
            is_updated = self.product_repository.update(product_id, product.to_entity())
            if not is_updated:
                return BaseResponse.error(
                    "Product updating failed.", "Product not found."
                )
            return BaseResponse.success("Product updated successfully.", None)
        except Exception:
            return BaseResponse.error(
                "Error updating product.", "Internal server error."
            )

    def delete(self, product_id: ObjectId) -> BaseResponse[None, str]:
        try:
            is_deleted = self.product_repository.delete(product_id)
            if not is_deleted:
                return BaseResponse.error(
                    "Product deletion failed.", "Product not found."
                )
            return BaseResponse.success("Product deleted successfully.", None)
        except Exception:
            return BaseResponse.error(
                "Error deleting product.", "Internal server error."
            )
