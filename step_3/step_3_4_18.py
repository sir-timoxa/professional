from datetime import date

def num_of_sundays(year):

    start = date(year,1,1).toordinal()
    end = date(year,12,31).toordinal()

    for x in range(start,start+7):
        if date.fromordinal(x).isoweekday()==7:
            new_start=x
            break
    counter=0

    for i in range(new_start,end+1,7):
        counter+=1

    return counter
