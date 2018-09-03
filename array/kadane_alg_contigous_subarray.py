# Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

n = [int(x) for x in input().split(' ')]

i = 0
curr_sum = n[0]
max_sum = -999999999
j = i+1
while j < len(n):
    curr_sum += n[j]
    if curr_sum >= max_sum:
        max_sum = curr_sum
        j += 1
    else:
        curr_sum = 0
        j += 1

print(max_sum)