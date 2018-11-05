# Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing,
# the missing number is to be found.
n = int(input())
array = [int(x) for x in input().split(' ')]

result1 = 0
for item in array:
    result1 ^= item
result2 = 0
for item in range(1, n+1):
    result2 ^= item
print(result1 ^ result2)
