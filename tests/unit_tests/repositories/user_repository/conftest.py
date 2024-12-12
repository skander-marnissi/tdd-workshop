import pytest

from tests.unit_tests.repositories.user_repository.data_mocks import user_data_sample, users_data_sample


@pytest.fixture
def user_data():
    return user_data_sample()

@pytest.fixture
def users_data():
    return users_data_sample()