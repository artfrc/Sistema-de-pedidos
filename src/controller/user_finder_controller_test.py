from .user_finder_controller import UserFinderController

class MockUser:
    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username

class MockRepository:

    def get_user_by_id(self, user_id):
        user = MockUser(user_id, "John Doe", "johndoe")
        return user
    
def test_finder_user():
    mock_repository = MockRepository()
    controller = UserFinderController(mock_repository)
    response = controller.finder_user(1)

    assert response == {
        'data': {
            'type': 'User', 
            'count': 1, 
            'attributes': {
                'id': 1, 
                'name': 'John Doe', 
                'username': 'johndoe'
            }
        }
    }