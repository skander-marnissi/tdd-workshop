from tests.integration_tests.views.user_view.data_mock import user_payload_sample, users_payload_sample, \
    users_data_sample
import pytest

USER_SERVICE_PATH = 'app.views.user_view.UserService'

@pytest.fixture
def create_user_payload():
    return user_payload_sample()

@pytest.fixture
def get_users_payload():
    return users_payload_sample()

@pytest.fixture
def get_users_data():
    return users_data_sample()


@pytest.fixture
def mock_get_users(mocker, get_users_data):
    user_service_mock = mocker.patch(USER_SERVICE_PATH)
    user_service_mock_instance = user_service_mock.return_value
    user_service_mock_instance.get_users.return_value = get_users_data

    return user_service_mock_instance
