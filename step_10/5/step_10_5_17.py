def primes(left, right):
    for num in range(left, right + 1):
        if num < 2:
            continue

        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            yield num



