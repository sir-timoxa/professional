
def get_digits(number: int | float) -> list[int]:
    return [int(x) for x in str(number) if x.isdigit()]


