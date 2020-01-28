"""
We are given a string S of length N consisting only of letters 'A and/or 'B'. Our goal is to obtain a string 
in the format "A...AB...B" (all letters 'A occur before all letter B) by deleting some letters from S.
In particular, strings consisting only of letters A or only of letters B fit this format.

Write a function:
	class Solution {public int solution(String S);}

that, given a string S, returns the minimum number of letters that need to be deleted from S in order to obtain
a string in the above format.

Examples:
	1. Given S = "BAAABAB", the fucntion should return 2, we can obtain "AAABB" by deleting the frist occurrence of B
	and the last occurrence of A
	2. Given S = "BBABAA", the function should return 3, we can delete all occurrence of A or all occurrence of B
	3. Given S = "AABBBB", return 0

Write an efficient algorithm for the following assumptions:
	* N is an integer within the range [1..100,000]
	* string S consists only of A and/or B

"""
