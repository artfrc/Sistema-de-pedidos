import re
from typing import  Dict
from src.models.sqlite.interfaces.users_repository_interface import IUserRepository
from src.models.sqlite.entities.users import UsersTable

class UserFinderController:
    def __init__(self, repository: IUserRepository):    
        self.__repository = repository

    def finder_user(self, user_id: int) -> UsersTable:
        self.__validate_user_id(user_id)
        user = self.__find_user_in_db(user_id)

        return self.__format_response(user)

    def __validate_user_id(self, user_id: int) -> None:
        
            no_valid_characters = re.compile(r"[^0-9]") # Expressão que aceita apenas números") 

            if no_valid_characters.search(str(user_id)):
                raise Exception("Invalid user_id")
            
    def __find_user_in_db(self, user_id: int) -> UsersTable:
         user = self.__repository.get_user_by_id(user_id)

         if not user:
             raise Exception("User not found")
         
         return user
    
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


    

    