from app.repositories.user_repository import UserRepository


class TestUserRepository:



    def test_add_user_with_valid_user_returns_updated_users_list(self, user_data):
        #Given
        user_repository = UserRepository()

        #When
        user_repository.add_user(user_data)

        #Then
        assert user_data in user_repository.users

    def test_get_all_users_returns_users_list(self, users_data):
        #Given
        user_repository = UserRepository()
        user_repository.users = users_data

        #When
        users = user_repository.get_all_users()

        #Then
        assert users == users_data