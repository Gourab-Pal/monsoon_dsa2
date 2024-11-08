'''
Given an array, find a non-empty contiguous subarray with the largest sum. 
Application of Kedan's algorithm
'''
def find_largest_contiguos_sum(arr):
    max_sum_so_far = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        max_sum_so_far = max(arr[i], max_sum_so_far+arr[i])
        if(max_sum_so_far>max_sum):
            max_sum = max_sum_so_far
    return max_sum

print(find_largest_contiguos_sum([-2,-3,4,-1,-2,1,5,-3]))