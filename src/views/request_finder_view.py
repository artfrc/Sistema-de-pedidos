from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.request_finder_controller_interface import IRequestFinderController
from .interfaces.view_interface import IView

class RequestFinderView(IView):
    def __init__(self, controller: IRequestFinderController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        request_id = request.param["id"]
        response = self.__controller.find_request(request_id)

        return HttpResponse(status_code=200, body=response)