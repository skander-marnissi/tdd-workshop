from app.models.user import User


def user_payload_sample():
    return {
        'id': "id_0",
        'firstname' : "Bob",
        'lastname' : "White",
        'email' : "bob.white@example.com",
        'age' : 35,
        'phone' : "555-5678"
        }

def users_data_sample():
    user_1 = User('id_0','Skander', 'Marnissi', 'skandermarnissi@xxx.com', 29, '555-5679')
    user_2 = User('id_1','George', 'Latel', 'george.latel@xxx.com', 30, '555-5678')
    user_3 = User('id_2','Malik', 'Lousabi', 'malik.lousabi@xxx.com', 32, '555-5680')
    return [user_1, user_2, user_3]