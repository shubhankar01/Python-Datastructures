# Given a number, check whether it is sparse or not. A number is said to be a sparse number
# if in binary representation of the number no two or more consecutive bits are set
t = int(input())
while t:
    n1 = int(input())
    count = 0
    flag =  False
    n2= n1>>1
    if n2 & n1:
        print(0)
    else:
        print(1)
    t-=1