# sample_code.py in main branch (correct code)

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print(add_numbers(5, 10))
print(divide_numbers(10, 2))  # No error

