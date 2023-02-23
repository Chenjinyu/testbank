"""
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

Example 1:
Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:
Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 
Constraints:
1 <= cards.length <= 105
0 <= cards[i] <= 106
"""
from collections import defaultdict
from typing import List
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        """
        The time complexity is still O(N) 
        even though we have a nested loop in the algorithm. This is because the inner loop in the nested loop can only iterate n times in total, since it's iterating over indices of elements from the array, where n is the length of the input array.
        JC - if the cards includes the same value, i think it can be a wrose case, if it is, the nested for loop only run once. so, the Time Complexity is O(N)
        """
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
            
        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
        return ans if ans < float("inf") else -1
            
            
    def minimumCardPickupImprove(self, cards: List[int]) -> int:    
        """
        We can actually improve this algorithm slightly by observing that we don't need to store all the indices, but only the most recent one that we saw for each number. This improves the average space complexity. The current algorithm has O(n) space complexity always, but with the improvement, it is only O(n) in the worst case, when there are no duplicates.
        """    
        dic = defaultdict(int)
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                ans = min(ans, i - dic[cards[i]] + 1)
            
            dic[cards[i]] = i

        return ans if ans < float("inf") else -1
    
    
    
cards = [3,4,2,3,3,4,7]
print(Solution().minimumCardPickupImprove(cards))