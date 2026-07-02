from functools import partial

def power(a: int, b: int) -> int:
    return a ** b

power_of_2 = partial(power, 2)

print(power_of_2(5))
