from app.models.user import User
from typing import List, Optional

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_all_users(self) -> List[User]:
        return self.users