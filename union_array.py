def union(arr1, arr2): # TC O(n+m)+O((n+m)log(n+m)) = O((n+m)log(n+m)), SC O(n+m)
    s = set()
    for item in arr1:
        s.add(item)
    for item in arr2:
        s.add(item)
    return sorted(s)

print(union([5,2,3], [5,1,0]))