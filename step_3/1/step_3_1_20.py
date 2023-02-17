from datetime import date

def get_min_max(dates):
    try:
        return min(dates),max(dates) 
    except:
        return ()

