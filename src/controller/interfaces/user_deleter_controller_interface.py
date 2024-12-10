from abc import ABC, abstractmethod

class IUserDeleterController(ABC):

    @abstractmethod
    def delete_user(self, user_id: int):
        pass        
