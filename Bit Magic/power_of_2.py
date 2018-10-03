t = int(input())
while t:
    n1 = int(input())
    n2= n1-1
    if n1==0:
        print('NO')
    else:
        if n1&n2:
            print('NO')
        else:
            print('YES')
    t-=1