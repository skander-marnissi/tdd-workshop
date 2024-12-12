import pytest
from app.services.user_service import UserService
from tests.unit_tests.services.user_service.data_mocks import create_user_data_payload, get_users_data

USER_REPOSITORY_PATH='app.services.user_service.UserRepository'

@pytest.fixture
def create_user_payload_fixture():
    return create_user_data_payload()

@pytest.fixture
def get_users_data_fixture():
    return get_users_data()

@pytest.fixture
def get_users_mock_fixture(mocker, get_users_data_fixture):
    user_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
    user_repository_mock_instance = user_repository_mock.return_value
    user_repository_mock_instance.get_all_users.return_value = get_users_data_fixture
    user_service = UserService()

    return user_service, user_repository_mock_instance

@pytest.fixture
def create_user_mock_fixture(mocker):
    user_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
    user_repository_mock_instance = user_repository_mock.return_value
    user_service = UserService()

    return user_service, user_repository_mock_instance