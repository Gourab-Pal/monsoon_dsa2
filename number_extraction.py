def extract_number(arr): # TC O(n), SC O(n)
    new_arr = []
    for item in arr:
        try:
            number = int(item)
            new_arr.append(number)
        except ValueError:
            continue
    return new_arr

def extract_number_optimised(arr): # TC O(n), SC O(1)
    last_integer_index = 0
    for item in arr:
        try:
            number = int(item)
            arr[last_integer_index] = number
            last_integer_index = last_integer_index + 1
        except:
            continue
    return arr[0:last_integer_index]

print(extract_number_optimised([1, "jk", "58", 47, 0, "0", "hello"]))