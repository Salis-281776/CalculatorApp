# advancedCalculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

# Advanced calculator functions
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def logarithm(x, base):
    return math.log(x, base)

# Example usage
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("3 * 7 =", multiply(3, 7))
print("15 / 3 =", divide(15, 3))
print("2 ^ 5 =", power(2, 5))
print("17 % 5 =", modulus(17, 5))
print("Factorial of 5 =", factorial(5))
print("Logarithm of 16 base 2 =", logarithm(16, 2))
