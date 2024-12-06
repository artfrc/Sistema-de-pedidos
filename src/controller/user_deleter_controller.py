import re
from src.models.sqlite.interfaces.users_repository_interface import IUserRepository

class UserDeleterController:
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    def delete_user(self, user_id: int):
        self.__validate_user_id(user_id)
        self.__delete_user_in_db(user_id)

    def __validate_user_id(self, user_id: int) -> None:
        
            no_valid_characters = re.compile(r"[^0-9]") # Expressão que aceita apenas números") 

            if no_valid_characters.search(str(user_id)):
                raise Exception("Invalid user_id")
            
    def __delete_user_in_db(self, user_id: int):
         self.__repository.delete_user(user_id)
        
