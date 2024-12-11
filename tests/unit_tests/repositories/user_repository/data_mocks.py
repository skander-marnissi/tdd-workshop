from app.models.user import User


def all_users_data():
    user_1 = User('Skander', 'Marnissi', 'skandermarnissi@xxx.com', 29, '555-5679')
    user_2 = User('George', 'Latel', 'george.latel@xxx.com', 30, '555-5678')
    user_3 = User('Malik', 'Lousabi', 'malik.lousabi@xxx.com', 32, '555-5680')
    return [user_1, user_2, user_3]

def add_user_data():
    return User('George', 'Latel', 'george.latel@xxx.com', 30, '555-5678')