from abc import ABC, abstractmethod
from typing import Dict

class IRequestCreatorController(ABC):

    @abstractmethod
    def create_request(self, request: Dict) -> Dict:
        pass