def filter_names(names, ignore_char, max_names):
    no_digits = (x for x in names if x.isalpha())
    no_ignore_char = (name for name in no_digits if not name.lower().startswith(ignore_char.lower()))
    return (name for idx, name in enumerate(no_ignore_char) if idx < max_names)



