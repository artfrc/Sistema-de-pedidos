from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.user_creator_controller_interface import IUserCreatorController
from .interfaces.view_interface import IView

class UserCreatorView(IView):
    def __init__(self, controller: IUserCreatorController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        user_info = request.body
        response = self.__controller.create_user(user_info)

        return HttpResponse(status_code=201, body=response)