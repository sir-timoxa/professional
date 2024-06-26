class LengthError(Exception):
    pass
class LetterError(Exception):
    pass
class DigitError(Exception):
    pass
import sys

def is_good_password(password):
    try:
        if len(password) < 9:
            raise LengthError('LengthError')
        elif not (any(x.islower() for x in password) and any(x.isupper() for x in password)):
            raise LetterError('LetterError')
        elif not any(x.isdigit() for x in password):
            raise DigitError('DigitError')
        else:
            print('Success!')
            return True
    except (LengthError, LetterError, DigitError) as err:
        print(err)
        return False
    

for line in sys.stdin:
    if is_good_password(str(line.rstrip('\n'))):
        break
