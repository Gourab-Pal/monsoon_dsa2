def reverse_words(my_str):
    word_list = my_str.split(" ")
    p1 = 0
    p2 = len(word_list) - 1
    while(p1<p2):
        tmp = word_list[p1]
        word_list[p1] = word_list[p2]
        word_list[p2] = tmp
        p1 += 1
        p2 -= 1
    return word_list

print(reverse_words("the sky is blue"))
