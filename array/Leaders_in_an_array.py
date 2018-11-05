# Given an array of positive integers. Your task is to find the leaders in the array.
# Note: An element of array is leader if it is greater than or equal to all the elements
# to its right side. Also, the rightmost element is always a leader.
n = [int(x) for x in input().split(' ')]
max_r = n[-1]
leaders = [n[-1]]
for i in range(len(n)-2,-1,-1):
    if n[i] >= max_r:
        max_r = n[i]
        leaders.insert(0,n[i])
print(leaders)
