import re
from src.models.sqlite.interfaces.requests_repository_interface import IRequestRepository

class RequestDeleterController:
    
    def __init__(self, repository: IRequestRepository):
        self.__repository = repository

    def delete_request(self, request_id: int):
        self.__validate_request_id(request_id)
        self.__delete_request_in_db(request_id)

    def __validate_request_id(self, request_id: int):
        no_valid_characters = re.compile(r"[^0-9]")  # Expressão que aceita apenas números

        if no_valid_characters.search(str(request_id)):
            raise Exception("Invalid user_id")
        
    def __delete_request_in_db(self, request_id: int):
        self.__repository.delete_request(request_id)
        