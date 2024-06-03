def no_cicles(n):
    if n > 0:
        print(n)
        no_cicles(n - 5)
    print(n)

