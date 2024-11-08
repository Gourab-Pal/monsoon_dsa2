'''
Given an array, find the element, partitioning along which, the sum of elements to its left, 
equals the sum of elements to its right. The partition element itself is to be excluded from both sums.

Return the index of the partitioning element. If no such element exists, return -1.
'''

def find_equal_partition_index(arr):
    left_sum = 0
    right_sum = 0
    for elem in arr:
        right_sum = right_sum + elem
    
    for i in range(len(arr)):
        right_sum = right_sum - arr[i]
        if(right_sum==left_sum):
            return i
        else:
            left_sum = left_sum + arr[i]
    return -1

print(find_equal_partition_index([1,4,2,5]))