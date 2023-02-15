from datetime import datetime, date


def change_date(gap):
    new_gap = gap.split('-')
    start = datetime.strptime(new_gap[0], '%d.%m.%Y').toordinal()
    end = datetime.strptime(new_gap[1], '%d.%m.%Y').toordinal()
    return [str(datetime.fromordinal(i)) for i in range(start, end+1)]


def is_available_date(booked_dates, date_for_booking):
    result_bd = []
    result_fb = []
    for x in booked_dates:
        if '-' in x:
            result_bd.extend(change_date(x))
        else:
            a = datetime.strptime(x, '%d.%m.%Y').toordinal()
            result_bd.append(str(datetime.fromordinal(a)))
    if '-' in date_for_booking:
        result_fb.extend(change_date(date_for_booking))
    else:
        a = datetime.strptime(date_for_booking, '%d.%m.%Y').toordinal()
        result_fb.append(str(datetime.fromordinal(a)))
    if set(result_bd) & set(result_fb):
        return False
    else: 
        return True
