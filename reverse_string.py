def reverse_string_version1(my_str): # TC O(n), SC O(n)
    char_list = []
    for i in range(len(my_str)-1, -1, -1):
        char_list.append(my_str[i])
    return "".join(char_list)

def reverse_string_version2(my_str): # TC O(n), SC O(n)
    char_list = list(my_str)
    p1 = 0
    p2 = len(char_list)-1
    while(p1<p2):
        tmp = char_list[p1]
        char_list[p1] = char_list[p2]
        char_list[p2] = tmp
        p1 += 1
        p2 -= 1
    return "".join(char_list)

print(reverse_string_version2("gourab"))