# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.
s = int(input())
n = [int(x) for x in input().split(' ')]
print()

i = 0
curr_sum = n[i]
le=len(n)
j = i+1
while j < len(n)+1:
    if curr_sum == s:
        print(i, j-1)
        break
    else:
        if j>=le:
            print(-1)
            break
        curr_sum += n[j]

    while curr_sum > s and i <j:
        curr_sum -= n[i]
        i += 1
    j += 1
print(curr_sum)
