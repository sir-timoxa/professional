def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]



numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)