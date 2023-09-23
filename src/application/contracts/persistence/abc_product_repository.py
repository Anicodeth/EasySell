from abc import ABCMeta, abstractmethod
from typing import List

from bson import ObjectId

from src.domain.entities.product import Product


class ABCProductRepository(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[Product]:
        pass

    @abstractmethod
    def add(self, product: Product) -> ObjectId:
        pass

    @abstractmethod
    def get(self, product_id: ObjectId) -> Product:
        pass

    @abstractmethod
    def update(self, product_id: ObjectId, product: Product) -> bool:
        pass

    @abstractmethod
    def delete(self, product_id: ObjectId) -> bool:
        pass

    @abstractmethod
    def get_user_products(self, user_id: str) -> bool:
        pass
