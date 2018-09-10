#code
t = int(input())
while t:
    try:
        s1 = input()
        s2 = input()
    except EOFError:
        pass
    if len(s1)!=len(s2):
        print('NO')
    else:
        for item in s2:
            if item in s1:
                s1= s1.replace(item, '' ,1)
                s2= s2.replace(item, '' ,1)
                pass
            else:
                print('NO')
                break
        print('YES')
    t -=1