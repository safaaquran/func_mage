from typing import Callable
from functools import wraps


def wrapper_func(f: Callable) -> Callable:
    @wraps(f)
    def returning_func() -> str:
        print("hi, welcome to wrap!")
        f()
        print("goodbye!")
    return returning_func


@wrapper_func
def func() -> str:
    print("safaa")


def response(min_gpa: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper_func(gpa: int):
            if gpa < min_gpa:
                return "sorry, you're not qualified for the internship"
            else:
                return func(gpa)
        return wrapper_func
    return decorator
        

@response(90)
def internship(gpa) -> str:
    return f"internship accepted with GPA: {gpa}"

func()
print(func.__name__)

print(internship(90))
