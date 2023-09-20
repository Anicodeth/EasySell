from abc import ABCMeta, abstractmethod
from typing import List

from bson import ObjectId

from Application.UseCases.DTOs.Product.create_product_dto import \
    CreateProductDto
from Application.UseCases.DTOs.Product.product_dto import ProductDto


class ProductServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[ProductDto]:
        pass

    @abstractmethod
    def add(self, product: CreateProductDto) -> ObjectId:
        pass

    @abstractmethod
    def get(self, id: ObjectId) -> ProductDto:
        pass

    @abstractmethod
    def update(self, id: ObjectId, product: CreateProductDto) -> None:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> None:
        pass
