def bee(n=1,times=16):
    if n < 4:
        print((f'{n}'*times).center(16))
        bee(n + 1,times-4)
    print((f'{n}'*times).center(16))

bee()