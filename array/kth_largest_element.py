a = [3,7,4,10,15,20]
def partition(a, l , r):
    pivot = a[l]
    while l < r:
        while pivot > a[l]:
            l += 1
        while pivot < a[r]:
            r -=1
        a[l],a[r] = a[r],a[l]
    pivot,a[l] = pivot,a[l]
    return l


def quickselect(a, l, r , k):
    if l< r:
        pindex = partition(a,l ,r)
        if pindex == k:
            return
        elif pindex < k:
            quickselect(a, pindex+1, r,k)
        else:
            quickselect(a, l, pindex-1,k)

quickselect(a,0,len(a)-1, 2)
print(a[2])