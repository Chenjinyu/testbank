"""
Find Even Digit
Find how many numbers have even digit in a list
Input: A = [12, 3, 5, 3456]
Output: 2
"""
def find_even_digit(A):
    return len([a for a in A if a % 2 == 0])

A = [12, 3, 5, 3456]
print(find_even_digit(A))