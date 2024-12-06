from typing import List, Dict
from src.models.sqlite.interfaces.users_repository_interface import IUserRepository
from src.models.sqlite.entities.users import UsersTable

class UserListerController:
    def __init__(self, repository: IUserRepository):    
        self.__repository = repository

    def list_users(self) -> List[UsersTable]:
        users = self.__list_users()

        return self.__format_response(users)

    def __list_users(self) -> List[UsersTable]:
        users = self.__repository.list_users()

        if not users:
            raise Exception("No users found")
        
        return users
    
    def __format_response(self, users: List[UsersTable]) -> Dict:
        return {
            "data": {
                "type": "List users",
                "count": len(users),
                "attributes": [
                    {
                        "id": user.id,
                        "name": user.name,
                        "username": user.username
                    }
                    for user in users
                ]
            }
        }