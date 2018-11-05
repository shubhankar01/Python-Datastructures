# Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[].
# The functions should put all 0s first, then all 1s and all 2s in last.
def sort012( a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid],a[hi] = a[hi],a[mid]
            hi = hi - 1
    return a
print(sort012( [2,2,0,0,1,1,1,2,0], len([2,2,0,0,1,1,1,2,0])))