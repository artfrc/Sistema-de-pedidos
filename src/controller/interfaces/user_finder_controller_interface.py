from abc import ABC, abstractmethod
from src.models.sqlite.entities.users import UsersTable

class IUserFinderController(ABC):

    @abstractmethod
    def finder_user(self, user_id: int) -> UsersTable:
        pass
    

    