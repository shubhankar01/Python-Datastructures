# Given an array and an integer k, find the maximum for each
# and every contiguous subarray of size k
t = int(input())
while t:
    s = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    n = s[0] - s[1] +1
    k = s[1]
    i =0

    while i < n:
        print(max(a[i:k]))
        i+=1
        k+=1
    print()
    t -=1