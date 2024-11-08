def find_max_occuring_char(my_str):
    char_dict = {}
    for i in range(len(my_str)):
        if my_str[i] in char_dict:
            char_dict[my_str[i]] += 1
        else:
            char_dict[my_str[i]] = 1
    
    max_occuring_char = " "
    max_occuring_count = 0
    for key in list(char_dict.keys()):
        if(char_dict[key]>max_occuring_count):
            max_occuring_count = char_dict[key]
            max_occuring_char = key
        elif(char_dict[key]==max_occuring_count):
            if(key<max_occuring_char):
                max_occuring_char = key

    return (max_occuring_char, max_occuring_count)

print(find_max_occuring_char("aaaSAAA"))