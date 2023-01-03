import re
import string

class InvalidLogin(Exception):
    pass


class InvalidPassword(Exception):
    pass


class InvalidEmail(Exception):
    pass


class Validation(Exception):
    pass


class Validator:
    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def validate_email(self):
        if "@" in self.email and self.email.endswith(".by") or self.email.endswith(".ru"):
            return True
        else:
            raise InvalidEmail

    def validate_login(self):
        if len(self.login) > 6:
            return True
        else:
            raise InvalidLogin

    def validate_password(self):
        if len(self.password) < 8 or len(set(self.password) & set(string.ascii_lowercase)) < 1 or len(
                set(self.password) & set(string.ascii_uppercase)) < 1 or len(
            set(self.password) & set(string.punctuation)) < 1:
            raise InvalidPassword
        else:
            return True

    def validation(self):
        try:
            self.validate_email()
            self.validate_login()
            self.validate_password()
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise Validation


valid_1 = Validator("Denis123", "denisVrbitski#", "denis.verbitski@mail.by")
valid_1.validation()