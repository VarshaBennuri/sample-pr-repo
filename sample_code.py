# sample_code.py

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    return a / b  # Might throw ZeroDivisionError

print(add_numbers(5, 10))
print(divide_numbers(10, 0))  # Buggy line
