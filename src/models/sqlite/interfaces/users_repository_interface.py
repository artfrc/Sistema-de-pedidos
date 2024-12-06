from abc import ABC, abstractmethod
from typing import List

from src.models.sqlite.entities.users import UsersTable

class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user: UsersTable):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> UsersTable:
        pass

    @abstractmethod
    def list_users(self) -> List[UsersTable]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass