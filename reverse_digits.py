def reverse_digits(n):
    if n==0:
        return 0
    elif n>0:
        reversed = 0
        while(n>0):
            last_digit = n%10
            quotient = int(n/10)
            reversed = reversed*10 + last_digit
            n = quotient
        return reversed
    else:
        tmp = abs(n)
        reversed = 0
        while(tmp>0):
            last_digit = tmp%10
            quotient = int(tmp/10)
            reversed = reversed*10 + last_digit
            tmp = quotient
        return reversed*(-1)

print(reverse_digits(-157))