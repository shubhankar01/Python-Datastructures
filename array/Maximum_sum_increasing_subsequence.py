# Given an array of n positive integers. Write a program to find
# the sum of maximum sum subsequence of the given array such that
# the integers in the subsequence are sorted in increasing order.

def maxSumIS(arr, n):
    max = 0
    msis = [0 for x in range(n)]

    # Initialize msis values for all indexes
    for i in range(n):
        msis[i] = arr[i]

    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            print (arr[i],'-',arr[j])
            if arr[i] > arr[j]:
                msis[i] = msis[j] + arr[i]

    # Pick maximum of all msis values
    print(msis)
    for i in range(n):
        if max < msis[i]:
            max = msis[i]

    return max
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing subsequence is " +
       str(maxSumIS(arr, n)))