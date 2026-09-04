def get_min_max(data):

    return None if not data else (min(enumerate(data),key=lambda x:x[1])[0], max(enumerate(data),key=lambda x:x[1])[0])




