t = int(input())
while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    s = a[0]
    for x in a[1:]:
        s = s ^ x
    print(s)
    t-=1