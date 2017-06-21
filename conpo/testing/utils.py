import json


def get_data_from_response(response, status_code=200):
    if status_code is not None:
        assert response.status_code == status_code

    if 'application/json' in response['content-type']:
        return json.loads(response.content.decode('utf-8'))

    return response.content
