from datetime import date


def get_date_range(date1, date2):
    try:
        f1 = int(date1.toordinal())
        f2 = int(date2.toordinal())
        if f2>f1:
            return [date.fromordinal(i) for i in range(f1, f2+1)]
        elif f2==f1:
            return [date1]
        else:
            return []
    except:
        return []

date1 = date(2025, 6, 5)
date2 = date(2022, 6, 6)
print(get_date_range(date1, date2))