import re
from typing import Dict, List
from src.controller.interfaces.request_finder_controller_interface import IRequestFinderController
from src.models.sqlite.entities.requests import RequestsTable
from src.models.sqlite.interfaces.requests_repository_interface import IRequestRepository

class RequestFinderController(IRequestFinderController):

    def __init__(self, repository: IRequestRepository):
        self.__repository = repository

    def find_request(self, request_id: int) -> RequestsTable:
        self.__validate_request_id(request_id)
        requests = self.__find_requests_in_db()

        return self.__format_response(requests)
    
    def __find_requests_in_db(self) -> List[RequestsTable]:
        requests = self.__repository.find_request()

        if not requests:
            raise Exception("No requests found")
        
        return requests
    
    def __validate_request_id(self, request_id: int):
        no_valid_characters = re.compile(r"[^0-9]")  # Expressão que aceita apenas números

        if no_valid_characters.search(str(request_id)):
            raise Exception("Invalid request_id")
        
    def __format_response(self, requests: List[RequestsTable]) -> Dict:
        return {
            "Type": "Request",
            "Count": 1,
            "Attributes": {
                    "request_id": requests.request_id,
                    "user_id": requests.user_id,
                    "description": requests.description,
                }
        }