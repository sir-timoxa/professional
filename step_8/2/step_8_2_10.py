def triangle(steps):
    if steps > 1:
        triangle(steps - 1)
    print('*' * steps)
    

triangle(3)