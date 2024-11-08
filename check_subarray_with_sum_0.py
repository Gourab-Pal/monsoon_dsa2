'''
Given an array of positive and negative numbers, you need to find if there is any subarray with 0 sum.

Note: A subarray of an array is a set of contiguous elements having a size of at least 1.
'''

def check_zero_sum_subarray(arr):
    s = set()
    current_sum = 0
    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        if((current_sum in s) | (current_sum==0)):
            return True
        else:
            s.add(current_sum)
    return False

print(check_zero_sum_subarray([4,2,-2,5]))