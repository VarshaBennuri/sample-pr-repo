# sample_code.py in feature branch (buggy code)

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    return a / b  # BUG: no zero check

print(add_numbers(5, 10))
print(divide_numbers(10, 0))  # BUG: division by zero
