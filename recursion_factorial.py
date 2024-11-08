def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return calculate_factorial(n-1)*n

print(calculate_factorial(0))