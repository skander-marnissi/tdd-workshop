class TestUserView:

    def setup_method(self):
        self.base_url = 'http://localhost:5000'
        self.get_users_url = f'{self.base_url}/users/'
        self.create_users_url = f'{self.base_url}/users/'

    def test_create_user_with_valid_data_returns_user(self, client, create_user_payload):
        #When
        response = client.post(self.create_users_url, json=create_user_payload)

        #Then
        assert response.status_code == 201
        assert response.json == create_user_payload

    def test_get_users_returns_users(self, client, get_users_payload, mock_get_users):
        #When
        response = client.get(self.get_users_url)

        #Then
        assert response.status_code == 200
        assert response.json == get_users_payload
        mock_get_users.get_users.assert_called_once()