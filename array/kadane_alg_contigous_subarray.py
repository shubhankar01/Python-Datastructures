# Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

n = [int(x) for x in input().split(' ')]

i = 0
curr_sum = 0
max_sum = -999999999
i = 0
while i < len(n):
    curr_sum += n[i]
    if curr_sum > max_sum:
        max_sum = curr_sum

    if curr_sum < 0:
        curr_sum = 0

    i += 1

print(max_sum)
