from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.user_lister_controller_interface import IUserListerController
from .interfaces.view_interface import IView

class RequestFinderView(IView):
    def __init__(self, controller: IUserListerController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        response = self.__controller.list_users()

        return HttpResponse(status_code=200, body=response)