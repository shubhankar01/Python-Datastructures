# code
t = int(input())
par = {'(': ')', '{': '}', '[': ']'}
while t:
    l = []
    s = input()
    check = True
    for x in s:
        if x in par.keys():
            l.append(x)
        else:
            if not l:
                check = False
                break
            else:
                elem = l.pop()
                if x == par[elem]:
                    pass
                else:
                    check = False
                    break
    if not l and check:
        print('balanced')
    else:
        print('not balanced')
    t -= 1