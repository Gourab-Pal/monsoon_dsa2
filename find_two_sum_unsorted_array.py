'''
Given an array of integers as input, output the indices of two numbers in the array which add up to a specified target.

Assume that each input would have exactly one solution and you cannot use the same element twice. 
If 2 different elements have the same value, they can be used.

Print the indices in increasing order.
'''

def two_sum_unsorted(arr, target):
    s = set()
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in s:
            idx1 = i
            break
        else:
            s.add(arr[i])
    for j in range(idx1):
        if(arr[j]==complement):
            idx2 = j
            break
    if(idx1<idx2):
        return (idx1, idx2)
    else:
        return  (idx2, idx1)

print(two_sum_unsorted([2,4,5,9,8], 7))