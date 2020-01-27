"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

from typing import List

class Solution:
    """
    basically, we can loop each number, and add the Fizz or(and) Buzz to string.
    what if we face a tricky interview and he decides to add too many mappings?
    having a condition for every mapping is not feasible or may be we can say the code might get ugly
    and tough to maintain.

    use Hash Table.
    """
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}    # add one more: "7": "Jazz"
        for num in range(1, n + 1):
            num_result_str = ""
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    num_result_str += fizz_buzz_dict[key]

            if num_result_str is "":
                num_result_str = str(num)
            result.append(num_result_str)

        return result
