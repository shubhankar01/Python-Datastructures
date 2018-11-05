t = int(input())


def pytha(a):
    for i in range(n):
        a[i] = a[i] * a[i]
    a.sort()
    count = 0
    for i in range(n - 1, 1, -1):
        k = i - 1
        j = 0
        while j < k:
            if a[i] == a[j] + a[k]:
                count = 1
                return True
            else:
                if a[j] + a[k] < a[i]:
                    j += 1
                else:
                    k -= 1
    return False


while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    if pytha(a):
        print('Yes')
    else:
        print('No')
    t -= 1