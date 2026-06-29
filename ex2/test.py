def test() -> int:
    age: int = 21
    def real():
        nonlocal age
        age = 22
    real()
    return age
print(test())
