'''
Given an array nums, you need to find the maximum sum of triplet (nums[i] + nums[j] + nums[k]) 
such that 0 <= i < j < k and nums[i] < nums[j] < nums[k]. If no such triplet exists print 0.
'''

def find_max_triplet_sum(arr):
    max_sum = 0
    for j in range(1, len(arr)-1):
        max_left = 0
        max_right = 0
        for i in range(0, j):
            if(arr[i]<arr[j]):
                max_left = max(max_left, arr[i])
        for k in range((j+1), len(arr)):
            if(arr[j]<arr[k]):
                max_right = max(max_right, arr[k])
        if((max_left>0) & (max_right>0)):
            curren_max_sum = max_left + arr[j] + max_right
            max_sum = max(max_sum, curren_max_sum)
    return max_sum

print(find_max_triplet_sum([3,7,4,2,5,7,5]))