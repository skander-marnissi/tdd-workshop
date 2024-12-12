from app.models.user import User


def user_payload_sample():
    return {
        "id": "id_0",
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "age": 30,
        "phone": "123456789"
    }

def users_payload_sample():
    return [
        {
            "id": "id_0",
            "firstname": "Skander",
            "lastname": "Marnissi",
            "email": "skandermarnissi@xxx.com",
            "age": 29,
            "phone": "555-5679"
        },
        {
            "id": "id_1",
            "firstname": "George",
            "lastname": "Latel",
            "email": "george.latel@xxx.com",
            "age": 30,
            "phone": "555-5678"
        },
        {
            "id": "id_2",
            "firstname": "Malik",
            "lastname": "Lousabi",
            "email": "malik.lousabi@xxx.com",
            "age": 32,
            "phone": "555-5680"
        }
    ]


def users_data_sample():
    user_1 = User('id_0','Skander', 'Marnissi', 'skandermarnissi@xxx.com', 29, '555-5679')
    user_2 = User('id_1','George', 'Latel', 'george.latel@xxx.com', 30, '555-5678')
    user_3 = User('id_2','Malik', 'Lousabi', 'malik.lousabi@xxx.com', 32, '555-5680')
    return [user_1, user_2, user_3]