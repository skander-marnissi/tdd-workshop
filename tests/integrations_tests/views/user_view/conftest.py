from tests.integrations_tests.views.user_view.data_mock import create_user_data_payload, get_users_data_payload, \
    get_users_data
import pytest

USER_SERVICE_PATH = 'app.views.user_view.UserService'

@pytest.fixture
def create_user_payload_fixture():
    return create_user_data_payload()

@pytest.fixture
def get_users_payload_fixture():
    return get_users_data_payload()

@pytest.fixture
def get_users_data_fixture():
    return get_users_data()


@pytest.fixture
def get_users_mock_fixture(mocker, get_users_data_fixture):
    user_service_mock = mocker.patch(USER_SERVICE_PATH)
    user_service_mock_instance = user_service_mock.return_value
    user_service_mock_instance.get_users.return_value = get_users_data_fixture

    return user_service_mock_instance
