# Given an array A your task is to tell at which position the
# equilibrium first occurs in the array. Equilibrium position
# in an array is a position such that the sum of elements below
# it is equal to the sum of elements after it.
n = [int(x) for x in input().split(' ')]


def equi(n):
    l = 0
    r = len(n) - 1
    left_sum = n[l]
    right_sum = n[r]
    while(l<=r):
        if left_sum == right_sum:
            l += 1
            r -= 1
            if l == r:
                print(n[l])
                return
            else:
                right_sum += n[r]
                left_sum += n[l]
        elif left_sum > right_sum:
            r-=1
            right_sum+=n[r]
        else:
            l+=1
            left_sum += n[l]
    print(-1)

equi(n)
