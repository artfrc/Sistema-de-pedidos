from abc import ABC, abstractmethod
from typing import Dict

class IUserCreatorController(ABC):

    @abstractmethod
    def create_user(self, user_info: Dict) -> Dict:
        pass