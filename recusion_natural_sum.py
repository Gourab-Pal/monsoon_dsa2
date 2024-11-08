def calculate_natural_sum(n):
    if n == 1:
        return n
    else:
        return calculate_natural_sum(n-1)+n

print(calculate_natural_sum(10))