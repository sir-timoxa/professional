def is_prime(number):
    if number != 1:
        return all(number % i != 0 for i in range(2, int(number**0.5) + 1))
    return False




