from .request_lister_controller import RequestListerController

class MockRequest:
    def __init__(self, request_id, description):
        self.request_id = request_id
        self.description = description

class MockRepository:
    def list_requests(self):
        request1 = MockRequest(1, "Test description 1")
        request2 = MockRequest(2, "Test description 2")
        return [request1, request2]
    
def test_list_requests():
    mock_repository = MockRepository()
    controller = RequestListerController(mock_repository)
    requests = controller.list_requests()

    assert requests == {
        'data': {
            'type': 'List requests', 
            'count': 2, 
            'attributes': [
                {
                    'request_id': 1, 
                    'description': 'Test description 1'}, 
                    {
                        'request_id': 2, 
                        'description': 'Test description 2'
                    }
            ]
        }
    }