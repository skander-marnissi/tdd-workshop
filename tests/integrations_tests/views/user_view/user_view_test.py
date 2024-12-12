class TestUserView:

    def setup_method(self):
        self.base_url = 'http://localhost:5000'
        self.get_users_url = f'{self.base_url}/users/'
        self.create_users_url = f'{self.base_url}/users/'

    def test_create_user_with_valid_data_returns_201(self, client, create_user_payload_fixture):
        #When
        response = client.post(self.create_users_url, json=create_user_payload_fixture)

        #Then
        assert response.status_code == 201
        assert response.json == create_user_payload_fixture

    def test_get_users_returns_200(self, client, get_users_payload_fixture, get_users_mock_fixture):
        #When
        response = client.get(self.get_users_url)

        #Then
        assert response.status_code == 200
        assert response.json == get_users_payload_fixture
        get_users_mock_fixture.get_users.assert_called_once()