from src.application.contracts.persistence.abc_product_repository import \
    ABCProductRepository
from src.application.contracts.persistence.abc_unit_of_work import \
    ABCUnitOfWork
from src.application.contracts.persistence.abc_user_repository import \
    ABCUserRepository
from src.persistence.db_client import DbClient
from src.persistence.repositories.product_repository import ProductRepository
from src.persistence.repositories.user_repository import UserRepository


class UnitOfWork(ABCUnitOfWork):
    def __init__(self):
        db_client = DbClient()
        self.user_repository = UserRepository(db_client)
        self.product_repository = ProductRepository(db_client)

    @property
    def user_repository(self) -> ABCUserRepository:
        return self._user_repository

    @user_repository.setter
    def user_repository(self, value):
        self._user_repository = value

    @property
    def product_repository(self) -> ABCProductRepository:
        return self._product_repository

    @product_repository.setter
    def product_repository(self, value):
        self._product_repository = value
