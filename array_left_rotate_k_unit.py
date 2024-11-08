def array_left_rotate_k(arr, k):
    while(k > 0):
        tmp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = tmp
        k = k - 1
    return arr

print(array_left_rotate_k([1,2,3,4,5], 2))

'''
TC = O(n*k)
SC = O(1)

'''