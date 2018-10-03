# You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.
t = int(input())
while t:
    n1,n2 = [int(x) for x in input().split()]
    count = 0
    n = n1^n2
    while n:
        n2=n-1
        n=n&n2
        count+=1
    print(count)
    t-=1