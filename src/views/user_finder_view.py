from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.interfaces.user_finder_controller_interface import IUserFinderController
from .interfaces.view_interface import IView

class UserFinderView(IView):
    def __init__(self, controller: IUserFinderController):
        self.__controller = controller
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        user_id = request.param["id"]
        response = self.__controller.finder_user(user_id)

        return HttpResponse(status_code=200, body=response)