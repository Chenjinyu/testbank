"""
Min Swaps to Group Red Balls

There are N balls positioned in a row, Each of them is either red or white.
In one move we can swap two adjacent balls.
We want to arrange all the red balls into a consistent segment.
What is the minimum number of swaps needed?

Write a function:
    class Solution {public int solution(String S);}
that, given string S of length N built from characters "R" and "W", representing red and white balls respectively.
returns the minimum number of swaps needed to arrange all the red balls into a consistent segment.
If the result exceedes 10^9, return -1.

Example:
    1. Given S = "WRRWWR", your function should return 2. we can move the last ball two positions to the left:
        * WRRWRW
        * WRRRWW
    2. Given S = "WWRWWWRWR", should return 4:
        * WWWRWWRWR
        * WWWWRWRWR
        * WWWWWRRWR
        * WWWWWRRRW
    3. Given S = "WWW", return 0
    4. Given S is "RW" repeated 100,000 times, should return -1. coz the minmum needed number of swaps is greater than 10^9

Write an efficient algorithm for the following assumptions:
    * N is an integer within the range [1..200,000]
    * string S consists only "R" and/or "W"

Related problems:

Minimum swaps need to make K girls sitting together: https://leetcode.com/discuss/interview-question/125154/
"""