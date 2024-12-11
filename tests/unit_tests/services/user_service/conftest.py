import pytest
from app.services.user_service import UserService
from tests.unit_tests.services.user_service.data_mocks import create_user_data_payload, get_users_data

USER_REPOSITORY_PATH='app.services.user_service.UserRepository'

@pytest.fixture
def create_user_fixture():
    return create_user_data_payload()

@pytest.fixture
def get_users_fixture():
    return get_users_data()

@pytest.fixture
def get_users_mock_fixture(mocker, get_users_fixture):
    mock_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
    mock_repository_instance = mock_repository_mock.return_value
    mock_repository_instance.get_all_users.return_value = get_users_fixture
    user_service = UserService()

    return user_service, mock_repository_instance

@pytest.fixture
def create_user_mock_fixture(mocker, get_users_fixture):
    mock_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
    mock_repository_instance = mock_repository_mock.return_value
    user_service = UserService()

    return user_service, mock_repository_instance