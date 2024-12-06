from src.models.sqlite.entities.users import UsersTable
from .user_creator_controller import UserCreatorController


class MockRepository:
    def create_user(self, user: UsersTable):
        pass

def test_create_user():
    user = {
        "name": "John Doe",
        "username": "johndoe",
        "password": "123456"
    }
    controller = UserCreatorController(MockRepository())
    response = controller.create_user(user)

    assert response == {
        'data': {
            'type': 'User', 
            'count': 1, 
            'attributes': {
                'id': None, 
                'name': 'John Doe', 
                'username': 'johndoe'}
        }
    }