def print_pyramid_right(n):
    for i in range(1,n+1):
        if i == n:
            print("*"*i)
        else:
            print("*"*i + " ")

print_pyramid_right(4)