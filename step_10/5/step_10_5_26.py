def palindromes():
    n = 1
    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n+=1



