# Given an unsigned integer N, swap all odd bits with even bits.
#  For example, if the given number is 23 ( 0 0 0 1 0 1 1 1 ),
# it should be converted to 43 ( 0 0 1 0 1 0 1 1 ). Here every
# even position bit is swapped with adjacent bit on right side
# (even position bits are highlighted in binary representation of 23),
# and every odd position bit is swapped with adjacent on left side.
t = int(input())
while t:
    n = int(input())
    # Get all even bits of x
    even_bits = n & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = n & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    print(even_bits | odd_bits)
    t -= 1