"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 
Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
"""
from collections import defaultdict, Counter
from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_dict = defaultdict(int)
        loser_dict = defaultdict(int)
        for match in matches:
            winner_dict[match[0]] += 1
            loser_dict[match[1]] += 1
            
        winner_set = set(winner_dict.keys())
        loser_set = set(loser_dict.keys())
        return [sorted(list(winner_set - loser_set)), sorted(list([loser for loser, times in loser_dict.items() if times == 1] ))]
    

    def findWinnersCounter(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set([x for x, _ in matches])
        losers = Counter([x for _, x in matches])
        
        return [
            sorted(winners - losers.keys()), sorted([k for k, v in losers.items() if v == 1])
        ]
    
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution().findWinnersCounter(matches))