# code
t = int(input())
while t:
    s = [int(x) for x in input().split()]
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    i = 0
    result = {}
    output = []
    j = 0
    while i < s[0]:
        if a1[i] in result.keys():
            result[a1[i]].append(a1[i])
        else:
            result[a1[i]] = []
            result[a1[i]].append(a1[i])
        i += 1
    for x in a2:
        if x in result.keys():
            output += result[x]
            del (result[x])

    for x in sorted(result):
        output += result[x]
    for x in output:
        print(x)
    print()
    t -= 1