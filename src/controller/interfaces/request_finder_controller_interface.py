from abc import ABC, abstractmethod
from src.models.sqlite.entities.requests import RequestsTable

class IRequestFinderController(ABC):

    @abstractmethod
    def find_request(self, request_id: int) -> RequestsTable:
        pass