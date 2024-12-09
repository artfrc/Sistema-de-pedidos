import re
from src.models.sqlite.entities.requests import RequestsTable
from src.models.sqlite.interfaces.requests_repository_interface import IRequestRepository

class RequestFinderController:

    def __init__(self, repository: IRequestRepository):
        self.__repository = repository

    def find_request(self, request_id: int) -> RequestsTable:
        self.__validate_request_id(request_id)

        return self.__repository.find_request(request_id)
    
    def __validate_request_id(self, request_id: int):
        no_valid_characters = re.compile(r"[^0-9]")  # Expressão que aceita apenas números

        if no_valid_characters.search(str(request_id)):
            raise Exception("Invalid request_id")