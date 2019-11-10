"""
Count Primes
Count the number of prime numbers less than(没有) a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import math
from collections import Counter
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        A prime number is a whole number greater than 1 whose only factors are 1 and itself.
        Method: Sieve of Eratosthenes
        :param n:
        :return:
        """
        isPrime = [True] * n
        # 0, 1 is not prime number. start from 2.
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        # print([x for x in range(2, n) if isPrime[x]])
        # ignore 0, 1 indexes.
        return Counter(isPrime[2:])[True]

    def countPrimes2(self, n: int) -> int:
        """
        A prime number is a whole number greater than 1 whose only factors are 1 and itself.
        Method: Sieve of Eratosthenes
        :param n:
        :return:
        """
        isPrime = [True] * (n + 1)
        # 1 is not prime number. start from 2
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
        return [x for x in range(2, n + 1) if isPrime[x]]

if __name__ == "__main__":
    print(Solution().countPrimes(10))