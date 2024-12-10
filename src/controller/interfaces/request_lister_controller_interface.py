from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.requests import RequestsTable

class IRequestListerController(ABC):

    @abstractmethod
    def list_requests(self) -> List[RequestsTable]:
        pass