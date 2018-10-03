t = int(input())
y = lambda a: a[0:4]
while t:
    result = {}
    n = int(input())
    arr = []
    a = [int(x) for x in input().split()]
    for x in a:
        temp = x
        x = str(x)

        if len(x) < 2:
            item = int(y(x + x + x + x))
        else:
            item = int(y(x + x))
        if item in result.keys():
            result[item] += x
        else:
            result[item] = x
            arr.append(item)
            # arr = result.keys()
    arr.sort(reverse=True)
    r = ''
    # print(result)
    # print(arr)
    for x in arr:
        r += result[x]
    print(r)
    t -= 1