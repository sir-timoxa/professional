def triangle(steps):
    def rec(steps):
        if steps > 0:
            print('*' * steps)
            rec(steps - 1)
    rec(steps)

