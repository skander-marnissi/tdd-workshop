import pytest

from tests.unit_tests.repositories.user_repository.data_mocks import add_user_data, all_users_data


@pytest.fixture
def add_user_fixture():
    return add_user_data()

@pytest.fixture
def get_all_users_fixture():
    return all_users_data()