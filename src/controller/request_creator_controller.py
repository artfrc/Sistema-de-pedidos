import re
from typing import Dict
from src.models.sqlite.entities.requests import RequestsTable
from src.models.sqlite.interfaces.requests_repository_interface import IRequestRepository

class RequestCreatorController:

    def __init__(self, repository: IRequestRepository):
        self.__repository = repository

    def create_request(self, request: Dict) -> Dict:
        description = request["description"]
        request_id= request["request_id"]

        self.__validate_request_id(request_id)
        request = RequestsTable(description, request_id)
        self.__repository.create_request(request)

        return self.__format_response(request)


    def __validate_request_id(self, request_id: int):
        no_valid_characters = re.compile(r"[^0-9]")  # Expressão que aceita apenas números

        if no_valid_characters.search(str(request_id)):
            raise Exception("Invalid user_id")
        
    def __format_response(self, request: RequestsTable) -> Dict:
        return {
            "data": {
                "type": "Request",
                "count": 1,
                "attributes": {
                    "id": request.id,
                    "description": request.description,
                    "request_id": request.user_id
                }
            }
        }