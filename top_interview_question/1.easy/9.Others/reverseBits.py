"""
Reverse Bits
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.


Follow up:

If this function is called many times, how would you optimize it?

Note:
after I search, although '0b' starts at the begin of binary number.
eg.
print(bin(2**32 - 1)) .                 --> 0b11111111111111111111111111111111
print(bin(1)) --> 0b1 if zfill it, could be 0b000000000000000000000000000001
you will realized the 0b is not include in the 32 binary string. add 0b, the string length is 34.
remove the '0b' and use int(binary_number, 2). 2 mean binary to int. 

'0b' signs it is a binary string. but in the int(binary_number, 2), it will convert the binary to int. the 0b is not necessary.
0b only a sign for it's a binary string, for this question, we want to reverse, so have to keep 32 bits.

did you really understand why there is no need to add '0d' at the begin of binary string?
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # return int('0b' + (bin(n)[2:]).zfill(30)[::-1], 2)
        return int((bin(n)[2:]).zfill(32)[::-1], 2)

if __name__ == "__main__":
    n = 45
    print(Solution().reverseBits(n))
    print(bin(n)[2:].zfill(32)[::-1])
