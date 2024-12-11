class TestUserService:
    def test_create_user_with_valid_data_return_valid_user(self, create_user_mock_fixture, create_user_fixture):
        # Given
        user_service, mock_repository_instance = create_user_mock_fixture

        # When
        user = user_service.create_user(create_user_fixture['firstname'],
                                             create_user_fixture['lastname'],
                                             create_user_fixture['email'],

                                             create_user_fixture['age'],
                                             create_user_fixture['phone'])

        # Then
        mock_repository_instance.add_user.assert_called_once()
        assert user.firstname == create_user_fixture['firstname']
        assert user.lastname == create_user_fixture['lastname']
        assert user.email == create_user_fixture['email']
        assert user.age == create_user_fixture['age']
        assert user.phone == create_user_fixture['phone']


    def test_get_users_return_valid_users(self, get_users_mock_fixture, get_users_fixture):
        # Given
        user_service, mock_repository_instance = get_users_mock_fixture

        # When
        users = user_service.get_users()

        # Then
        mock_repository_instance.get_all_users.assert_called_once()
        assert len(users) == 3
        assert users[0] == get_users_fixture[0]
        assert users[1] == get_users_fixture[1]
        assert users[2] == get_users_fixture[2]