def array_rotate_left(arr):
    tmp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = tmp
    return arr

print(array_rotate_left([1,2,3,4,5]))

'''
TC = O(n)
SC = O(1)

'''