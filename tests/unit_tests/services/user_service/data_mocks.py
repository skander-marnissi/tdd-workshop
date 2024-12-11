from app.models.user import User


def create_user_data_payload():
    return {
        'firstname' : "Bob",
        'lastname' : "White",
        'email' : "bob.white@example.com",
        'age' : 35,
        'phone' : "555-5678"
        }

def get_users_data():
    user_1 = User('Skander', 'Marnissi', 'skandermarnissi@xxx.com', 29, '555-5679')
    user_2 = User('George', 'Latel', 'george.latel@xxx.com', 30, '555-5678')
    user_3 = User('Malik', 'Lousabi', 'malik.lousabi@xxx.com', 32, '555-5680')
    return [user_1, user_2, user_3]