from typing import Dict, List
from bson import ObjectId
from pymongo import MongoClient

from Application.UseCases.DTOs.Product.create_product_dto import CreateProductDto
from Application.UseCases.DTOs.Product.product_dto import ProductDto
from Application.Contracts.iproduct_repository import ProductRepositoryInterface

conn_string = "mongodb+srv://afmtoday:OlxwPFCF0rLMnA3e@cluster0.edrrjyh.mongodb.net/easysell?retryWrites=true&w=majority"

class ProductRepository(ProductRepositoryInterface):
    def __init__(self, data: List[Dict[str, object]]):
        self.data = data
        self.client = MongoClient(conn_string)
        self.db = self.client.rentomatic
        self.products = self.db.products

    def list(self) -> List[ProductDto]:
        return [ProductDto.from_dict(product) for product in list(self.products.find())]

    def add(self, product: CreateProductDto) -> ObjectId:
        product_id = self.products.insert_one(product).inserted_id
        return product_id

    def get(self, id: ObjectId) -> ProductDto:
        return ProductDto.from_dict(self.products.find_one({"_id": id}))

    def update(self, id: ObjectId, product: CreateProductDto) -> None:
        return self.products.update_one({"_id": id}, {"$set": product.to_dict()})

    def delete(self, id: ObjectId) -> None:
        return self.products.delete_one({"_id": id})
