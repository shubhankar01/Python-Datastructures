t = int(input())
while t:
    s = int(input())
    a1= [int(x) for x in input().split()]
    i=0
    result ={}
    output = []
    j = 0
    while i< s:
        if a1[i] in result.keys():
            result[a1[i]][0].append(a1[i])
            result[a1[i]][1] += 1
        else:
            result[a1[i]] = [[]]
            result[a1[i]][0].append(a1[i])
            result[a1[i]].append(1)
        i+=1
    for x in sorted(result.items(), key=lambda x: x[1][1], reverse=True):
        for y in x[1][0]:
            print(y)
    print()
    t -=1