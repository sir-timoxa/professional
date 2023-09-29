from collections import OrderedDict

def custom_sort(ordered_dict,by_values=False):
    if not by_values:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
        return ordered_dict
    else:
        for x in sorted(ordered_dict.items(),key=lambda item: item[1]):
            ordered_dict.move_to_end(x[0])
        return ordered_dict
            