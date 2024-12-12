from typing import List
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()


    def create_user(self, user_id: str, firstname: str, lastname: str, email: str, age: int, phone: str) -> User:
        user = User(user_id, firstname, lastname, email, age, phone)
        self.repository.add_user(user)
        return user

    def get_users(self) -> List[User]:
        return self.repository.get_all_users()