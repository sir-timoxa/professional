def is_good_password(password):
    if len(password)>=9 and any(x.isdigit() for x in password) and any(x.islower() for x in password) and any(x.isupper() for x in password):
        return True
    else:
        return False
