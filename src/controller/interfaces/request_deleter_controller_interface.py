from abc import ABC, abstractmethod

class IRequestDeleterController(ABC):
    
    @abstractmethod
    def delete_request(self, request_id: int):
        pass        