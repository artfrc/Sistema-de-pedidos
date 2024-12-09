from .request_finder_controller import RequestFinderController

class MockRequest:
    def __init__(self, request_id):
        self.request_id = request_id
        self.description = "Test description"

class MockRepository:
    def find_request(self, request_id):
        request = MockRequest(request_id)
        return request
    
def test_find_request():
    mock_repository = MockRepository()
    controller = RequestFinderController(mock_repository)
    request = controller.find_request(1)

    assert request.request_id == 1
    assert request.description == "Test description"