def count_unique_chars(my_str):
    s = set()
    for i in range(len(my_str)):
        s.add(my_str[i])
    return len(s)

print(count_unique_chars("hello"))