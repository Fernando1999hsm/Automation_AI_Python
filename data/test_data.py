from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str


class TestData:
    standard_user = User(username="standard_user", password="secret_sauce")
    problem_user = User(username="problem_user", password="secret_sauce")
    invalid_user = User(username="usuario_invalido", password="password_invalido")
