from .request_finder_controller import RequestFinderController

class MockRequest:
    def __init__(self):
        self.request_id = 1
        self.description = "Test description"
        self.user_id = 1

class MockRepository:
    def find_request(self):
        request = MockRequest()
        return request
    
def test_find_request():
    mock_repository = MockRepository()
    controller = RequestFinderController(mock_repository)
    request = controller.find_request(1)

    assert request == {
        'Type': 'Request', 
        'Count': 1, 
        'Attributes': {
            'request_id': 1, 
            'user_id': 1, 
            'description': 'Test description'
        }
    }