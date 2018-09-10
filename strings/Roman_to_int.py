t = int(input())
look_up = {'I':1, 'V': 5, 'X': 10,  'L':50, 'C': 100, 'D':500, 'M':1000}
while t:
    s = input()
    result = 0
    prev = s[0]
    for x in s:
        if look_up[prev]<look_up[x]:
            result +=look_up[x]-2*look_up[prev]
        else:
            result +=look_up[x]
        prev= x
    t -=1
    print(result)