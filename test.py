from functools import partial, partialmethod, cmp_to_key

def power(x: int, y: int) -> int:
    return x**y


power_of_5 = partial(power, 1)

print(power_of_5(2))


class Demo:
    def __init__(self):
        self.color = 'black'

    def _color(self, type):
        self.color = type


    set_blue = partialmethod(_color, 'blue')
    set_green = partialmethod(_color, type='green')
    set_red = partialmethod(_color, "red")

obj = Demo()
print(obj.color)
obj.set_red()
print(obj.color)

def compare_func(a, b) -> int:
    if a[-1] > b[-1]:
        return 1
    elif a[-1] < b[-1]:
        return -1
    else:
        return 0

logo: list[str] = ["fortytwo", "born2code", "born2code"]
sorted_logo: list[str] = sorted(logo, key=cmp_to_key(compare_func))
print(f"sorted logo : {sorted_logo}")
