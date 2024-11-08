'''
Given a sorted array of integers and a target, find if there’s a pair of elements that add up to the target. 
Return true if such a pair can be found, and false otherwise.
'''

def check_pair(arr, target): #TC O(n), bruteforce TC O(n**2)
    p1 = 0
    p2 = len(arr) - 1
    pair_sum = 0
    while(p1<p2):
        pair_sum = arr[p1] + arr[p2]
        if(pair_sum==target):
            return True
        elif(pair_sum<target):
            p1 += 1
        else:
            p2 -= 1
    return False

print(check_pair([2,4,5,8,9], 7))