from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.request_deleter_controller_interface import IRequestDeleterController
from .interfaces.view_interface import IView

class RequestDeleterView(IView):
    def __init__(self, controller: IRequestDeleterController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        id_request = request.param["id"]
        self.__controller.delete_request(id_request)

        return HttpResponse(status_code=204)