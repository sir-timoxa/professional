def choose_plural(x, data):
    if str(x)[-2::] in ('11', '12', '13', '14'):
        return str(x)+' '+str(data[2])
    elif str(x)[-1] == '1':
        return str(x)+' '+str(data[0])
    elif str(x)[-1] in ('2','3','4'):
        return str(x)+' '+ str(data[1])
    else:
        return str(x)+' '+str(data[2])