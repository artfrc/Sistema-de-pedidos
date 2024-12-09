from .request_creator_controller import RequestCreatorController

class MockRepository:
    def create_request(self, request):
        pass

def test_create_request():
    repository = MockRepository()
    controller = RequestCreatorController(repository)
    request = {
        "description": "Test description",
        "request_id": 1
    }
    response = controller.create_request(request)

    assert response == {
        'data': {
            'type': 'Request', 
            'count': 1, 
            'attributes': {
                'id': None, 
                'description': 'Test description', 
                'request_id': 1
            }
        }
    }