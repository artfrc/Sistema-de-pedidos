from .user_deleter_controller import UserDeleterController

def test_delete_user(mocker):
    repository = mocker.Mock()
    controller = UserDeleterController(repository)
    controller.delete_user(1)

    repository.delete_user.assert_called_once_with(1)