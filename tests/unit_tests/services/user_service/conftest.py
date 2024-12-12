import pytest
from tests.unit_tests.services.user_service.data_mocks import user_payload_sample, users_data_sample

USER_REPOSITORY_PATH='app.services.user_service.UserRepository'

@pytest.fixture
def create_user_payload():
    return user_payload_sample()

@pytest.fixture
def get_users_data():
    return users_data_sample()

@pytest.fixture
def mock_user_repository_get_all_users(mocker, get_users_data):
    user_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
    user_repository_mock_instance = user_repository_mock.return_value
    user_repository_mock_instance.get_all_users.return_value = get_users_data

    return user_repository_mock_instance

@pytest.fixture
def mock_user_repository(mocker):
    user_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
    user_repository_mock_instance = user_repository_mock.return_value


    return user_repository_mock_instance

# @pytest.fixture
# def mock_user_repository(mocker):
#     def make(instance_path=USER_REPOSITORY_PATH,spy=False,**kwargs):
#         user_repository_mock = mocker.patch(USER_REPOSITORY_PATH)
#         user_repository_mock_instance = user_repository_mock.return_value
#         return customer
#
#     return make

