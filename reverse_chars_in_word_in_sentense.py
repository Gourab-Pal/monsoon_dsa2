def reverse_string(my_str): # TC O(n), SC O(n)
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

def reverse_chars_in_long_string(my_str):
    word_list = my_str.split(" ")
    for i in range(len(word_list)):
        word_list[i] = reverse_string(word_list[i])
    return " ".join(word_list)

print(reverse_chars_in_long_string("my name is gourab"))