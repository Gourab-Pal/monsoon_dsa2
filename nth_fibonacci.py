def get_nth_fibonacci(n):
    if((n==0) | (n==1)):
        return n
    else:
        return get_nth_fibonacci(n-2) + get_nth_fibonacci(n-1)
    
print(get_nth_fibonacci(6))