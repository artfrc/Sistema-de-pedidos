from typing import Dict, List
from src.controller.interfaces.request_lister_controller_interface import IRequestListerController
from src.models.sqlite.entities.requests import RequestsTable
from src.models.sqlite.interfaces.requests_repository_interface import IRequestRepository

class RequestListerController(IRequestListerController):

    def __init__(self, repository: IRequestRepository):
        self.__repository = repository

    def list_requests(self) -> List[RequestsTable]:
        requets = self.__list_requests()

        return self.__format_response(requets)

    def __list_requests(self) -> List[RequestsTable]:
        requests = self.__repository.list_requests()

        if not requests:
            raise Exception("No requests found")

        return requests
    
    def __format_response(self, requests: List[RequestsTable]) -> Dict:
        return {
            "data": {
                "type": "List requests",
                "count": len(requests),
                "attributes": [
                    {
                        "request_id": request.request_id,
                        "description": request.description
                    }
                    for request in requests
                ]
            }
        }