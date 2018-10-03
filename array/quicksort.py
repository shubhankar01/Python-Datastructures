a = [2,1,3,4,5,6]
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


def quicksort(a, l, r):
    if  l< r:
        pindex = partition(a,l ,r)
        quicksort(a, pindex+1, r)
        quicksort(a, l, pindex-1)

quicksort(a,0,len(a)-1)
print(a)