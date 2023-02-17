
s =[input() for _ in range(3)]


en = all(map(lambda x: x in 'AaBCcEeHKMOoPpTXxy',s))
ru = all(map(lambda x: x in 'АаВСсЕеНКМОоРрТХху',s))

if ru:
    print('ru')
elif en:
    print('en')
else:
    print('mix')

