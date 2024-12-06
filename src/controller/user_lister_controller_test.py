from .user_lister_controller import UserListerController

class MockUser:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username

class MockRepository:

    def list_users(self):
        user1 = MockUser(1, "John Doe", "johndoe")
        user2 = MockUser(2, "Jane Doe", "janedoe")
        return [user1, user2]

def test_list_users():
    mock_repository = MockRepository()
    controller = UserListerController(mock_repository)
    response = controller.list_users()

    assert response == {
        'data': {
            'type': 'List users', 
            'count': 2, 
            'attributes': [
                {
                    'id': 1, 
                    'name': 'John Doe', 
                    'username': 'johndoe'}, 
                    {
                        'id': 2, 
                        'name': 'Jane Doe', 
                        'username': 'janedoe'
                    }
            ]
        }
    }