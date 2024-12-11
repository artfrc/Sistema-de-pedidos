from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.user_deleter_controller_interface import IUserDeleterController
from .interfaces.view_interface import IView

class UserDeleterView(IView):
    def __init__(self, controller: IUserDeleterController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        id_user = request.param["id"]
        self.__controller.delete_request(id_user)

        return HttpResponse(status_code=204)