"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1)
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Example 1:
Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input:
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""
from typing import List
import operator

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Beat: 15.24%
        """
        cost_and_gas = list(zip(gas, cost))
        length_zip = len(cost_and_gas)
        idx = 0

        def circuit_helper(cost_and_gas, index):
            total_tank, curr_tank = 0, 0
            for idx, val in enumerate(cost_and_gas[index:] + cost_and_gas[:index]):
                cur_gas, cur_cost = val
                total_tank += (cur_gas - cur_cost)
                if total_tank < 0:
                    return False, idx + index + 1
            return True, index

        for _ in range(length_zip):
            is_can, idx = circuit_helper(cost_and_gas, idx)
            if is_can:
                return idx

        return -1

    def canCompleteCircuitImprove(self, gas: List[int], cost: List[int]) -> int:
        """
        beats 99.41%
        """
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

    def canCompleteCircuitImprove2(self, gas: List[int], cost: List[int]) -> int:
        """
        does not work. because, the curr_tank should be cumulated。
        """
        # new_list = list(map(lambda x, y: x - y, gas, cost))
        new_list = list(map(operator.sub, gas, cost))
        starting_station = [v for v in new_list if v >= 0]
        return starting_station[0] if sum(new_list) >= 0 else -1


if __name__ == "__main__":
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]


    # new_list = list(map(lambda x, y: x - y, gas, cost))
    # new_list = list(map(operator.sub, gas, cost))
    # print(new_list)
    # cost_and_gas = list(zip(gas, cost))
    # print(cost_and_gas[0:] + cost_and_gas[:0])

    print(Solution().canCompleteCircuitImprove2(gas, cost))
