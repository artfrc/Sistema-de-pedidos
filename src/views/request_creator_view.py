from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.request_creator_controller_interface import IRequestCreatorController
from .interfaces.view_interface import IView

class RequestCreatorView(IView):
    def __init__(self, controller: IRequestCreatorController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        request_info = request.body
        response = self.__controller.create_request(request_info)

        return HttpResponse(status_code=201, body=response)