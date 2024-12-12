from app.repositories.user_repository import UserRepository


class TestUserRepository:



    def test_add_user(self, add_user_data_fixture):
        #Given
        user_repository = UserRepository()

        #When
        user_repository.add_user(add_user_data_fixture)

        #Then
        assert add_user_data_fixture in user_repository.users

    def test_get_all_users(self, get_all_users_data_fixture):
        #Given
        user_repository = UserRepository()
        user_repository.users = get_all_users_data_fixture

        #When
        users = user_repository.get_all_users()

        #Then
        assert users == get_all_users_data_fixture