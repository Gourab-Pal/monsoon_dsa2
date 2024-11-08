def check_integer_palindrome(my_int):
    input_int = my_int
    rev_num = 0
    while(my_int>0):
        rem = my_int%10
        quo = my_int//10
        rev_num = rev_num*10 + rem
        my_int = quo
    return rev_num==input_int

print(check_integer_palindrome(121))