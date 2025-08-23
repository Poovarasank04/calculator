def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("1 + 2 =", add(1, 2))
    print("5 - 3 =", sub(5, 3))
    print("4 * 2 =", mul(4, 2))
    print("8 / 2 =", div(8, 2))
