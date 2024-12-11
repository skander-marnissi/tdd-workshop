from dataclasses import dataclass, field

@dataclass
class User:
    firstname: str
    lastname: str
    email: str
    age: int
    phone: str