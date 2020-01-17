"""
1268. Search Suggestions System

Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names
from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]


Constraints:
1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""
from typing import List
from bisect import insort
from collections import defaultdict


class Trie:
    def __init__(self):
        # lambda function, nested() assign defaultdict(nested) data type to self.trie
        nested = lambda: defaultdict(nested)
        self.trie = nested()
        self.word = defaultdict(list)

    def add(self, word):
        trie = self.trie
        for ch in word:
            trie = trie[ch]
            insort(self.word[id(trie)], word)

    def search(self, word):
        trie = self.trie
        for ch in word:
            trie = trie[ch]
            yield self.word[id(trie)][:3]


class Solution:
    """
    Amazon OA Problem
    """
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        for product in products:
            trie.add(product)

        return list(trie.search(searchWord))


if __name__ == "__main__":
    testcases = [
        {
            'products': [
                "mobile", "mouse", "moneypot", "monitor", "mousepad"
            ],
            'searchWord': "mouse",
            'e': [
                    ["mobile", "moneypot", "monitor"],
                    ["mobile", "moneypot", "monitor"],
                    ["mouse", "mousepad"],
                    ["mouse", "mousepad"],
                    ["mouse", "mousepad"]
                ]
         },
        {
            'products': [
                "havana"
            ],
            'searchWord': "havana",
            'e': [
                    ["havana"],
                    ["havana"],
                    ["havana"],
                    ["havana"],
                    ["havana"],
                    ["havana"]
            ]
        },
        {
            'products': [
                "bags", "baggage", "banner", "box", "cloths"
            ],
            'searchWord': "bags",
            'e': [
                    ["baggage", "bags", "banner"],
                    ["baggage", "bags", "banner"],
                    ["baggage", "bags"],
                    ["bags"]
            ]
        },
    ]
    for case in testcases:
        actual_result = Solution().suggestedProducts(case['products'], case['searchWord'])
        print("Input: {}\nExpected: {}\nAcutal: {}\nis_Passed: {}".format(case['products'],
                                                                          case['e'],
                                                                          actual_result,
                                                                          actual_result == case['e']))