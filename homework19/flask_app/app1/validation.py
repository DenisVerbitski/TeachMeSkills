import re


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
        if re.match(r'^[\w.-]+@[\w.-]+\.(\S{2}$)', self.email):
            return True
        else:
            raise InvalidEmail

    def validate_login(self):
        if re.match(r'[0-9a-zA-Z]{6,10}$', self.login):
            return True
        else:
            raise InvalidLogin

    def validate_password(self):
        if not re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[$%#^])[0-9a-zA-Z$%#^]{8,}$', self.password):
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
        return True