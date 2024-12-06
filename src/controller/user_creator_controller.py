import re # EXpressões regulares
from typing import Dict
from src.models.sqlite.interfaces.users_repository_interface import IUserRepository
from src.models.sqlite.entities.users import UsersTable

class UserCreatorController:
    def __init__(self, repository: IUserRepository):    
        self.__repository = repository

    def create_user(self, user_info: Dict) -> Dict:
        name = user_info["name"]
        username = user_info["username"]
        password = user_info["password"]

        self.__validate_name(name)
        self.__validate_username(username)
        user = UsersTable(name, username, password)
        self.__create_user_in_db(user)

        return self.__format_response(user)

    def __validate_name(self, name: str):

        no_valid_characters = re.compile(r"[^a-zA-Z ]") # Expressão que aceita apenas letras e espaços

        if no_valid_characters.search(name):
            raise Exception("Invalid name")
        
    def __validate_username(self, username: str):
        
        no_valid_characters = re.compile(r"[^a-zA-Z0-9]") # Expressão que aceita apenas letras e números

        if no_valid_characters.search(username):
            raise Exception("Invalid username")
        
    def __create_user_in_db(self, user: UsersTable):
        self.__repository.create_user(user)

    def __format_response(self, user: UsersTable) -> Dict:
        return {
            "data": {
                "type": "User",
                "count": 1,
                "attributes": {
                    "id": user.id,
                    "name": user.name,
                    "username": user.username
                }
            }
        }