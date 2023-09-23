from typing import List

from bson import ObjectId

from src.application.contracts.persistence.product_repository_contract import \
    ProductRepositoryContract
from src.domain.entities.product import Product
from src.persistence.db_client import DbClient
from src.persistence.models.product_model import ProductModel


class ProductRepository(ProductRepositoryContract):
    def __init__(self, db: DbClient):
        self.products = db.get_collection("products")

    def list(self) -> List[Product]:
        return list(map(Product.from_dict, self.products.find()))

    def add(self, product: Product) -> ObjectId:
        product_id = self.products.insert_one(ProductModel.from_entity(product).to_dict()).inserted_id
        return product_id

    def get(self, product_id: ObjectId) -> Product:
        return Product.from_dict(self.products.find_one({"_id": product_id}))

    def update(self, product_id: ObjectId, product: Product) -> bool:
        status = self.products.update_one({"_id": product_id}, {"$": ProductModel.from_entity(product).to_dict()})
        return status.modified_count > 0

    def delete(self, product_id: ObjectId) -> bool:
        status = self.products.delete_one({"_id": product_id})
        return status.deleted_count > 0
