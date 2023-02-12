first = input()

glas = 'а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', '')
soglas = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ'.replace(
    ', ', '')

f1 = list(map(lambda x: 1 if x in glas else 0, first))


for i in range(int(input())):
    flag = True
    word = input()
    f2 = list(map(lambda x: 1 if x in glas else 0, word))
    for x, y in zip(f1, f2):
        if x != y:
            flag = False
    if f1.count(1) != f2.count(1):
        flag = False
    if flag:
        print(word)
