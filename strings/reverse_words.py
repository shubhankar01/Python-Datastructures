t = int(input())
while t:
    s = input().split('.')
    s = s[::-1]
    t -= 1
    result = ''
    for item in s:
        result += item + '.'
    result = result[0:-1]
    print(result)
