def is_palindrome(text):
    if text == '' or len(text) == 0:
        return True
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

print(is_palindrome('stepik'))
print(is_palindrome('level'))
print(is_palindrome('122333221'))
