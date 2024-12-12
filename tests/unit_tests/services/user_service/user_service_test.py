from app.services.user_service import UserService


class TestUserService:
    def test_create_user_with_valid_user_returns_user(self, mock_user_repository, create_user_payload):
        # Given
        user_service = UserService()
        user_repository_mock_instance = mock_user_repository

        # When
        user = user_service.create_user(create_user_payload['id'],
                                            create_user_payload['firstname'],
                                             create_user_payload['lastname'],
                                             create_user_payload['email'],
                                             create_user_payload['age'],
                                             create_user_payload['phone'])

        # Then
        user_repository_mock_instance.add_user.assert_called_once()
        assert user.id == create_user_payload['id']
        assert user.firstname == create_user_payload['firstname']
        assert user.lastname == create_user_payload['lastname']
        assert user.email == create_user_payload['email']
        assert user.age == create_user_payload['age']
        assert user.phone == create_user_payload['phone']


    def test_get_users_returns_users_list(self, mock_user_repository_get_all_users, get_users_data):
        # Given
        user_service = UserService()
        user_repository_mock_instance = mock_user_repository_get_all_users

        # When
        users = user_service.get_users()

        # Then
        user_repository_mock_instance.get_all_users.assert_called_once()
        assert len(users) == 3
        assert users[0] == get_users_data[0]
        assert users[1] == get_users_data[1]
        assert users[2] == get_users_data[2]