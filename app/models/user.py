from dataclasses import dataclass, field

@dataclass
class User:
    id:str
    firstname: str
    lastname: str
    email: str
    age: int
    phone: str