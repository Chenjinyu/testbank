"""
Find Most Common
Input: A = [2, 2, 3, 3, 5]
Output: [2, 3]
"""

from collections import Counter

def find_most_common(A):
    counter_a = Counter(A)
    # get the maximum count
    most_common_count = max(counter_a.values())
    # get how many maximum it has
    count_common = list(counter_a.values()).count(most_common_count)
    return [val[0] for val in counter_a.most_common(count_common)]

A = [2, 2, 3, 3, 5]
print(find_most_common(A))