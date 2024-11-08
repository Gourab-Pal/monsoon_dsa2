def find_max_occuring_word(my_list):
    word_dict = dict()
    for word in my_list:
        if(word in word_dict):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    max_occuring_word = " "
    max_occuring_count = 0
    for key in list(word_dict.keys()):
        if(word_dict[key]>max_occuring_count):
            max_occuring_count = word_dict[key]
            max_occuring_word = key
        elif(word_dict[key]==max_occuring_count):
            if(key<max_occuring_word): # lexicographically minimum word is chosen
                max_occuring_word = key
    return (max_occuring_word, max_occuring_count)

print(find_max_occuring_word(["my", "name", "is", "gourab", "the", "name", "is", "unique"]))