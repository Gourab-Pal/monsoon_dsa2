'''
Given an integer array, find the largest subarray with sum 0 . 
If there is more than one subarray with the largest length, return the subarray with the lowest starting index.

If there is no such sub-array print -1.
'''

def find_largest_zero_subarray(arr):
    total_so_far = arr[0]
    total = arr[0]
    d = dict()
    for i in range(1, len(arr)):
        total_so_far = total_so_far + arr[i]
        