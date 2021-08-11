from rest_framework.exceptions import ValidationError
from re import search


class Validator:

    def __init__(self, data):
        for field in data:
            try:
                method = getattr(self, field)
                method(data[field])
            except AttributeError:
                ...

    def password(self, password):
        passLen = len(password)
        if (passLen < 6 or passLen > 30):
            raise ValidationError(detail='Senha inválida.')

    def email(self, email):
        regex = r'^[\w_.+-]+@[\w-]+\.[\w.-]+$'
        if not search(regex, email):
            raise ValidationError(detail='Email inválido.')

    def name(self, name):
        regex = r"[^A-Za-zÀ-Ÿà-ÿ\s']"
        if search(regex, name):
            raise ValidationError(detail='Invalid name.')

    def username(self, username):
        regex = r"[^A-Za-zÀ-Ÿà-ÿ0-9]"
        if search(regex, username):
            raise ValidationError(detail='Invalid username.')
