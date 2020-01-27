"""
3. Max Network Rank

An infrastructure consisting of N cities, numbered from 1 to N, and M bidirectional roads between them is given.
Roads do not intersect apart from at their start and end points
(they can pass through underground tunnels to avoid collisions)

For each pair of cities directly connected by a road, let's define their network rank as the total number of
roads that are connected to either of the two cities:

Write a function:
    class Solution {public int solution(int[] A, int[] B, int N);}

that, given two arrays A, B consisting of M integers each and an integer N, where A[i] and B[i] are cities
at the ends of the i-th road, return the maximal network rank in the whole infrastructure.

Example1:
    Given A = [1,2,3,3], B=[2,3,1,4] and N = 4, the function should return 4.
    the chosen cities may be 2 and 3, and the four roads connected to them are:
    (2,1), (2,3), (3,1), (3,4)

In the picture below, the chosen cities and roads connected to them are marked in red.
"""


