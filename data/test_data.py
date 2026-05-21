from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str


class TestData:
    standard_user = User(username="standard_user", password="secret_sauce")
    problem_user = User(username="problem_user", password="secret_sauce")
    invalid_user = User(username="usuario_invalido", password="password_invalido")

class TestErrorMessages:
    USERNAME_REQUIRED = "Epic sadface: Username is required"
    INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"