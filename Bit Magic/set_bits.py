# Given a positive integer N, print count of set bits in it.
# For example, if the given number is 6, output should be 2 as there are two set bits in it.
t = int(input())
while t:
    n1 = int(input())
    count = 0
    while n1:
        n2=n1-1
        n1=n1&n2
        count+=1
    print(count)
    t-=1