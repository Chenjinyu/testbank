"""
157. Read N Characters Given Read4

Given a file and assume that you can only read the file using a given method read4,
implement a method to read n characters.

"""

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

def read4(buf):
    return 4


class Solution:
    """
    Facebook OA Problem
    """
    def read(self, buf, n):
        ans = 0
        while True:
            buffer = [""] * 4
            read_char = read4(buffer)
            min_char = min(read_char, n)
            n = n - 4
            buf[ans: ans + min_char] = buffer[0: min_char]
            ans = ans + min_char
            if read_char < 4 or n <= 0:
                break

        return ans
