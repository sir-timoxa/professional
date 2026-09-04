def all_together(*objects):
    return (i
            for elem in objects
                for i in elem)



