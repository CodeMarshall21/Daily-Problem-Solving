# Position of rightmost different bit using XOR:
Get the bitwise xor of m and n. Let it be xor_value = m ^ n. Now, find the position of rightmost set bit in xor_value. As 0 XOR 1 and 1 XOR 0 equals 1, so if a bit is set in the XOR value then it means that the bits at that position were different in the given numbers

## An efficient way to find the rightmost set bit: 
log2(n & -n) + 1 gives us the position of the rightmost set bit.<br>
(-n) reverses all the bits from left to right till the last set bit


for example: n = 16810 <br>
binary signed 2’s complement of n  = 00000000101010002 <br>
binary signed 2’s complement of -n = 11111111010110002 <br>
? (n & -n) = 00000000000010002 = 8 <br>
now, log2(n & -n) = log2(8) = 3 <br>
log2(n & -n) + 1 = 4 (position of rightmost set bit) <br>
