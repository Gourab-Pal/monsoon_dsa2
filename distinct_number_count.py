def find_distint_count(my_list): # TC O(n), SC O(n)
    s = set()
    for item in my_list:
        s.add(item)
    return len(s)

print(find_distint_count([1,2,2,3,2,4]))