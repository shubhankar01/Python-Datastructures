# Given an array of n positive integers. Write a program to find
# the sum of maximum sum subsequence of the given array such that
# the integers in the subsequence are sorted in increasing order.

def maxSumIS(arr, n):
    max = 0
    msis = [0 for x in range(n)]

    # Initialize msis values for all indexes
    for i in range(n):
        msis[i] = arr[i]
    max_l = 1
    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        l = 1
        for j in range(i):
            if arr[i] > arr[j]:
                msis[i] = msis[j] + arr[i]
                l += 1
                print (arr[i], '-', arr[j])
                if l>max_l:
                    max_l = l

    # Pick maximum of all msis values
    for i in range(n):
        if max < msis[i]:
            max = msis[i]

    return max_l,max
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing subsequence is " +
       str(maxSumIS(arr, n)))