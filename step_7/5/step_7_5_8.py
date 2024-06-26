class LengthError(Exception):
    pass
class LetterError(Exception):
    pass
class DigitError(Exception):
    pass

try:
    def is_good_password(password):
        if len(password)<9:
            raise LengthError
        elif not (any(x.islower() for x in password) and any(x.isupper() for x in password)):
            raise LetterError
        elif not any(x.isdigit() for x in password):
            raise DigitError
        else:
            return True
except (LengthError,LetterError,DigitError):
    pass

