from abc import ABCMeta, abstractmethod

from src.application.contracts.persistence.abc_product_repository import \
    ABCProductRepository
from src.application.contracts.persistence.abc_user_repository import \
    ABCUserRepository


class ABCUnitOfWork(metaclass=ABCMeta):
    @property
    @abstractmethod
    def user_repository(self) -> ABCUserRepository:
        pass

    @property
    @abstractmethod
    def product_repository(self) -> ABCProductRepository:
        pass
