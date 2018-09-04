# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.
s = int(input())
n = [int(x) for x in input().split(' ')]

i = 0
curr_sum = n[i]
j = i+1
while j < len(n):
    if curr_sum == s:
        print(i, j-1)
        break
    else:
        curr_sum += n[j]

    while curr_sum > s and i <=j-1:
        curr_sum -= n[i]
        i += 1
    j += 1