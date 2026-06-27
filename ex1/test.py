from typing import Callable

name: str = "safaa"
print(callable(name))

def name_returning(name : str) -> str:
    return name

f: Callable[[str], str] = name_returning
print(callable(f))
print(f("safaa"))
