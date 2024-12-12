from app.models.user import User


def create_user_data_payload():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "age": 30,
        "phone": "123456789"
    }

def get_users_data_payload():
    return [
        {
            "firstname": "Skander",
            "lastname": "Marnissi",
            "email": "skandermarnissi@xxx.com",
            "age": 29,
            "phone": "555-5679"
        },
        {
            "firstname": "George",
            "lastname": "Latel",
            "email": "george.latel@xxx.com",
            "age": 30,
            "phone": "555-5678"
        },
        {
            "firstname": "Malik",
            "lastname": "Lousabi",
            "email": "malik.lousabi@xxx.com",
            "age": 32,
            "phone": "555-5680"
        }
    ]


def get_users_data():
    user_1 = User('Skander', 'Marnissi', 'skandermarnissi@xxx.com', 29, '555-5679')
    user_2 = User('George', 'Latel', 'george.latel@xxx.com', 30, '555-5678')
    user_3 = User('Malik', 'Lousabi', 'malik.lousabi@xxx.com', 32, '555-5680')
    return [user_1, user_2, user_3]