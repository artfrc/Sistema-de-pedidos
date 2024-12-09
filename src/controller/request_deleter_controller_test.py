from .request_deleter_controller import RequestDeleterController

def test_delete_user(mocker):
    repository = mocker.Mock()
    controller = RequestDeleterController(repository)
    controller.delete_request(1)

    repository.delete_request.assert_called_once_with(1)