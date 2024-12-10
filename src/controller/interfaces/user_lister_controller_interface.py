from abc import ABC, abstractmethod
from typing import List

from src.models.sqlite.entities.users import UsersTable

class IUserListerController(ABC):

    @abstractmethod
    def list_users(self) -> List[UsersTable]:
        pass