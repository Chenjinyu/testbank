"""
Given a string, output the run length encoding of that string so that repeat letters are compressed to the character and count.
Example:
abcccddeeeeea => abc3d2e5a

"""

def compressString(sub_str):
    compress_str = ""
    sub_len = len(sub_str)
    count = 1
    first_char = sub_str[0]
    for i in range(1, sub_len):
        if sub_str[i] == first_char:
            count += 1
        else:
            compress_str += first_char + str(count if count > 1 else "")
            first_char = sub_str[i]
            count = 1

        # check i if reach to end of element
        # and add the last element to compress_str
        if i == sub_len - 1:
            compress_str += first_char + str(count if count > 1 else "")

    return compress_str


if __name__ == "__main__":
    sub_str = "abcccddeeeeea"
    print(compressString(sub_str))

