from abc import ABC, abstractmethod
from typing import List

from src.models.sqlite.entities.requests import RequestsTable

class IRequestRepository(ABC):

    @abstractmethod
    def create_request(self, request: RequestsTable):
        pass

    @abstractmethod
    def get_request_by_id(self, request_id: int) -> RequestsTable:
        pass

    @abstractmethod
    def list_requests(self) -> List[RequestsTable]:
        pass

    @abstractmethod
    def delete_request(self, request_id: int):
        pass