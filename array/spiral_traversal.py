#a= [[1,2,3,4,5, 6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
a = [[1,2,3,4],[5, 6,7,8],[9,10,11,12],[13,14,15,16]]
k = 0
l = 0
n = len(a)
m = len(a[0])
while k < m and l < n:
    i = l
    while i < m:
        print(a[k][i],end = ' ')
        i+=1
    k+=1
    i = k
    while i< m:
        print(a[i][n-1],end = ' ')
        i+=1
    n-=1

    if k < m:
        i = n-1
        while i >= l:
            print(a[m-1][i], end = ' ')
            i-=1
        m-=1
    if l<n:
        i  = m-1
        while i >= k:
            print(a[i][l],end = ' ')
            i-=1
        l+=1