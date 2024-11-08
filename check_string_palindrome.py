def check_string_palindrome(my_str): # TC O(n), SC(1)
    if my_str==" ":
        return True
    else:
        p1 = 0
        p2 = len(my_str) - 1
        while(p1<p2):
            if (my_str[p1]==my_str[p2]):
                p1 += 1
                p2 -= 1
            else:
                return False
            return True
    
print(check_string_palindrome("madam"))