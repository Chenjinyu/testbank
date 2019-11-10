from collections import defaultdict

class Solution:
    def normal_fibonacci(self, n):
        """
        the time complexity is O(2^n)
        although it has while loop, let's walk through each call:
        fib(1) -> 2^1 steps
        fib(2) -> 2^2 steps
        fib(3) -> 2^3 steps
        fib(4) -> 2^4 steps
        ...
        fib(n) -> 2^n steps
        """
        fib_list = []
        while n > 0:
            fib_list.append(self.fib(n))
            n -= 1
        return fib_list

    def fib(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    def fibonacci_memoization(self, n):
        """
        the time complexity is O(n).
        This technique, called memoization, is a very common one to optimize exponential time recursive algorithms.
        store the last sum value in cache_map.
        """
        cache_map = defaultdict()
        fib_list = []
        while n > 0:
            fib_list.append(self.fib2(n, cache_map))
            n -= 1
        return fib_list

    def fib2(self, n, cache_map):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache_map.keys() and cache_map[n] > 0:
            return cache_map[n]

        cache_map[n] = self.fib2(n - 1, cache_map) + self.fib2(n - 2, cache_map)
        return cache_map[n]


if __name__ == "__main__":
    # print(Solution().normal_fibonacci(200))  # Limited Time Exceeded.
    print(Solution().fibonacci_memoization(200))
