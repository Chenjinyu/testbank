"""
Concatenated String Length with unique Characters

Given an Array A consisting of N Strings, calculate the length of the longest string S such that:

S is a concatenation of some of the Strings from A.
every letter in S is different.
Example -
A = ["co","dil","ity"] , function should return 5, resulting string S could be codil , dilco, coity,ityco
A = ["abc","kkk","def","csv"] , returns 6 , resulting Strings S could be abcdef , defabc, defcsv , csvdef
A = ["abc","ade","akl"] , return 0 , impossible to concatenate as letters wont be unique.

N is [1..8] ; A consists of lowercase English letters ; sum of length of strings in A does not exceed 100.

Related problems:

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""

def unique_character(A):
    pass


A = ["co","dil","ity"]
print(unique_character(A))

A = ["abc","kkk","def","csv"]
print(unique_character(A))

A = ["abc","ade","akl"]
print(unique_character(A))