import source.service as service
import unittest.mock as mock
import requests
import pytest


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Luis"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Luis"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Leanne Graham"}
    mock_get_return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "Leanne Graham"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get_return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()