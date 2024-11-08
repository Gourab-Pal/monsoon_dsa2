def find_index(arr, target): # binary search, TC O(logn), SC O(n)
    begin = 0
    end = len(arr)-1
    while(begin<end):
        mid = (begin + end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            begin = mid + 1
        elif(arr[mid]>target):
            end = mid - 1
    return -1

print(find_index([2, 7, 8, 10,18], 8))