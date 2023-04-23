from src.api.requests import get_request


def api_get_test():
    
    response_get = get_request()

    assert 'status' in response_get, 'Error in API status.'
    assert response_get['status'] == 'OK', 'API is not started.'

    return response_get


if __name__ == "__main__":
    api_get_test()