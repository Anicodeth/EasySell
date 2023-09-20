from typing import List

from bson import ObjectId

from Application.Contracts.iproduct_repository import \
    ProductRepositoryInterface
from Application.Contracts.iproduct_service import ProductServiceInterface
from Application.UseCases.DTOs.Product.create_product_dto import \
    CreateProductDto
from Application.UseCases.DTOs.Product.product_dto import ProductDto


class ProductService(ProductServiceInterface):
    def __init__(self, product_repository: ProductRepositoryInterface) -> None:
        self.product_repository = product_repository

    def list(self) -> List[ProductDto]:
        return self.product_repository.list()

    def add(self, product: CreateProductDto) -> ObjectId:
        return self.product_repository.add(product)

    def get(self, id: ObjectId) -> ProductDto:
        return self.product_repository.get(id)

    def update(self, id: ObjectId, product: CreateProductDto) -> None:
        self.product_repository.update(id, product)

    def delete(self, id: ObjectId) -> None:
        self.product_repository.delete(id)
