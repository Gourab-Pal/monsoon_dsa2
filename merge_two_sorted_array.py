'''

Given two sorted arrays of size M and N, merge the two arrays and return the final array, sorted.
'''

def merge_sorted(a1, a2):
    sorted_array = []
    m = len(a1)
    n = len(a2)
    p1 = 0
    p2 = 0
    while((p1<m) & (p2<n)):
        if(a1[p1]<a2[p2]):
            sorted_array.append(a1[p1])
            p1 += 1
        else:
            sorted_array.append(a2[p2])
            p2 += 1
    while(p1<m):
        sorted_array.append(a1[p1])
        p1 += 1
    while(p2<n):
        sorted_array.append(a2[p2])
        p2 += 1
    return sorted_array

print(merge_sorted([1,2,3], [2,5,6]))    
