import pytest

from tests_2023.mock_data import (
    render_test_nodes, 
    node_traversal, 
    m0713_test_array,
    m2270_test_nums
)

from data_structures_and_algorithms.c3_hashing.e0001_TwoSum import Solution as Sol0001
from data_structures_and_algorithms.c3_hashing.e2351_FirstLetterToAppearTwice import Solution as Sol2351
from data_structures_and_algorithms.c3_hashing.e1832_CheckIfTheSentenceIsPangram import Solution as Sol1832
from data_structures_and_algorithms.c3_hashing.e1426_CountingElements import Solution as Sol1426
from data_structures_and_algorithms.c3_hashing.e2248_IntersectionOfMultipleArrays import Solution as Sol22248
from data_structures_and_algorithms.c3_hashing.e1941_CheckIfAllCharactersHaveEqualNumberOfOccurences import Solution as Sol1941
from data_structures_and_algorithms.c3_hashing.m0560_SubarraySumEqualsK import Solution as Sol0560
from data_structures_and_algorithms.c3_hashing.m1248_CountNumberOfNiceSubarrays import Solution as Sol1248
from data_structures_and_algorithms.c3_hashing.m2225_FindPlayersWithZeroOrOneLosses import Solution as Sol2225
from data_structures_and_algorithms.c3_hashing.e1133_LargestUniqueNumber import Solution as Sol1133
from data_structures_and_algorithms.c3_hashing.e1189_MaximumNumberOfBalloons import Solution as Sol1189
from data_structures_and_algorithms.c3_hashing.m0049_GroupAnagrams import Solution as Sol0049
from data_structures_and_algorithms.c3_hashing.m2260_MinumumConsecutiveCardsToPickUp import Solution as Sol2260
from data_structures_and_algorithms.c3_hashing.m2342_MaxSumOfAPairWithEqualSumOfDigits import Solution as Sol2342
from data_structures_and_algorithms.c3_hashing.m2352_EqualRowAndColumnPairs import Solution as Sol2352
from data_structures_and_algorithms.c3_hashing.e0771_JewelsAndStones import Solution as Sol0771
from data_structures_and_algorithms.c3_hashing.m0003_LongestSubstringWithoutRepeatingCharacters import Solution as Sol0003
# bonus problems, hashing

# Checking for existence
from data_structures_and_algorithms.c3_hashing.e0217_ContainsDuplicate import Solution as Sol0217
from data_structures_and_algorithms.c3_hashing.e1436_DestinantionCity import Solution as Sol1436
from data_structures_and_algorithms.c3_hashing.e1496_PathCrossing import Solution as Sol1496
# Counting
from data_structures_and_algorithms.c3_hashing.e1748_SumOfUniqueElements import Solution as Sol1748
from data_structures_and_algorithms.c3_hashing.e1394_FindLuckyIntegerInAnArray import Solution as Sol1394
from data_structures_and_algorithms.c3_hashing.e1207_UnqiueNumberOfOccurrences import Solution as Sol1207
from data_structures_and_algorithms.c3_hashing.m0451_SortCharactersByFrequency import Solution as Sol0451
from data_structures_and_algorithms.c3_hashing.e1512_NumberOfGoodPairs import Solution as Sol1512
from data_structures_and_algorithms.c3_hashing.m0930_BinarySubarraysWithSum import Solution as Sol0930
from data_structures_and_algorithms.c3_hashing.m1695_MaximumErasureValue import Solution as Sol1695
from data_structures_and_algorithms.c3_hashing.m0567_PermutationInString import Solution as Sol0567

# General
from data_structures_and_algorithms.c3_hashing.e0205_IsomorphicStrings import Solution as Sol0205
from data_structures_and_algorithms.c3_hashing.m0791_CustomSortString import Solution as Sol0791
from data_structures_and_algorithms.c3_hashing.m1657_DetermineIfTwoStringsAreClose import Solution as Sol1657
from data_structures_and_algorithms.c3_hashing.e0290_WordPattern import Solution as Sol0290


@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([2,7,11,15], 9, [0, 1]),
    ([3,2,4], 6, [1, 2]),
    ([3,3], 6, [0, 1])
])
def test_twoSum(test_input1, test_input2, excepted_output):
    # assert Sol0001().twoSum(test_input1, test_input2) == excepted_output
    # assert Sol0001().twoSumRedo(test_input1, test_input2) == excepted_output
    # assert Sol0001().twoSumWithTwoPointers(test_input1, test_input2) == excepted_output
    assert Sol0001().twoSumWithHaskMap(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("abccbaacz", 'c'),
    ("abcdd", "d"),
])
def test_repeatedCharacter(test_input1, excepted_output):
    assert Sol2351().repeatedCharacter(test_input1) == excepted_output
    assert Sol2351().repeatedCharacterSet(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("leetcode", False),
])
def test_repeatedCharacter(test_input1, excepted_output):
    assert Sol1832().checkIfPangram(test_input1) == excepted_output
    assert Sol1832().checkIfPangramSet(test_input1) == excepted_output
    assert Sol1832().checkIfPangramCounter(test_input1) == excepted_output
    

@pytest.mark.parametrize("test_input1, excepted_output", [
    ([1,2,3], 2),
    ([1,1,3,3,5,5,7,7], 0),
    ([1 ,1,2, 2], 2)
])
def test_repeatedCharacter(test_input1, excepted_output):
    assert Sol1426().countElements(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], [3,4]),
    ([[1,2,3],[4,5,6]], []),
])
def test_intersection(test_input1, excepted_output):
    assert Sol22248().intersection(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("abacbc", True),
    ("aaabb", False),
])
def test_areOccurrencesEqual(test_input1, excepted_output):
    assert Sol1941().areOccurrencesEqual(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
])
def test_subarraySum(test_input1, test_input2, excepted_output):
    assert Sol0560().subarraySum(test_input1, test_input2) == excepted_output


@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([1,1,2,1,1], 3, 2),
    ([2,4,6], 1, 0),
    ([2,2,2,1,2,2,1,2,2,2], 2, 16),
])
def test_numberOfSubarrays(test_input1, test_input2, excepted_output):
    assert Sol1248().numberOfSubarrays(test_input1, test_input2) == excepted_output


@pytest.mark.parametrize("test_input1, excepted_output", [
    ([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]], [[1,2,10],[4,5,7,8]]),
    ([[2,3],[1,3],[5,4],[6,4]], [[1,2,5,6],[]]),
])
def test_findWinners(test_input1, excepted_output):
    assert Sol2225().findWinners(test_input1) == excepted_output
    assert Sol2225().findWinnersCounter(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([5,7,3,9,4,9,8,3,1], 8),
    ([9,9,8,8], -1),
])
def test_findWinners(test_input1, excepted_output):
    assert Sol1133().largestUniqueNumber(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("nlaebolko", 1),
    ("loonbalxballpoon", 2),
    ("leetcode", 0),
    ("balon", 0),
])
def test_maxNumberOfBalloons(test_input1, excepted_output):
    assert Sol1189().maxNumberOfBalloons(test_input1) == excepted_output
    

@pytest.mark.parametrize("test_input1, excepted_output", [
    (["eat","tea","tan","ate","nat","bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    ([""], [[""]]),
    (["a"], [["a"]]),
])
def test_groupAnagrams(test_input1, excepted_output):
    assert Sol0049().groupAnagrams(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([3,4,2,3,4,7], 4),
    ([3,4,2,3,3,4,7], 2),
    ([1,0,5,3], -1),
])
def test_minimumCardPickup(test_input1, excepted_output):
    assert Sol2260().minimumCardPickup(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([18,43,36,13,7], 54),
    ([10,12,19,14], -1),
    ([279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128], 872)
])
def test_maximumSum(test_input1, excepted_output):
    assert Sol2342().maximumSum(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3),
    ([[3,2,1],[1,7,6],[2,7,7]], 1),
])
def test_equalPairs(test_input1, excepted_output):
    assert Sol2352().equalPairs(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0),
])
def test_numJewelsInStones(test_input1, test_input2, excepted_output):
    assert Sol0771().numJewelsInStones(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test_lengthOfLongestSubstring(test_input1, excepted_output):
    assert Sol0003().lengthOfLongestSubstring(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
])
def test_containsDuplicate(test_input1, excepted_output):
    assert Sol0217().containsDuplicate(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], "Sao Paulo"),
    ([["B","C"],["D","B"],["C","A"]], "A"),
    ([["A","Z"]], "Z"),
])
def test_destCity(test_input1, excepted_output):
    assert Sol1436().destCity(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("NES", False),
    ("NESWW", True),
])
def test_isPathCrossing(test_input1, excepted_output):
    assert Sol1496().isPathCrossing(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([1,2,3,2], 4),
    ([1,1,1,1,1], 0),
    ([1,2,3,4,5], 15),
])
def test_sumOfUnique(test_input1, excepted_output):
    assert Sol1748().sumOfUnique(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [
  ([2,2,3,4], 2),
  ([1,2,2,3,3,3], 3),
  ([2,2,2,3,3], -1)
])
def test_findLucky(test_input, excepted_output):
    assert Sol1394().findLucky(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [
    ([1,2,2,1,1,3], True),
    ([1,2], False),
    ([-3,0,1,-3,1,1,1,-3,10,0], True)
])
def test_uniqueOccurrences(test_input, excepted_output):
    assert Sol1207().uniqueOccurrences(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [
    ("tree", "eert"),
    ("cccaaa", "aaaccc"),
    ("Aabb", "bbAa"),
])
def test_frequencySort(test_input, excepted_output):
    assert Sol0451().frequencySort(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [
    ([1,2,3,1,1,3], 4),
    ([1,1,1,1], 6),
    ([1,2,3], 0),
])
def test_numIdenticalPairs(test_input, excepted_output):
    assert Sol1512().numIdenticalPairs(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ("egg", "add", True),  
  ("foo", "bar", False),
  ("paper", "title", True),
])
def test_isIsomorphic(test_input1, test_input2, excepted_output):
    assert Sol0205().isIsomorphic(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ("abba", "dog cat cat dog", True),  
  ("abba", "dog cat cat fish", False),
  ("aaaa", "dog cat cat dog", True),
])
def test_wordPattern(test_input1, test_input2, excepted_output):
    assert Sol0290().wordPattern(test_input1, test_input2) == excepted_output
    
@pytest.mark.todo
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ([1,0,1,0,1], 2, 4),  
  ([0,0,0,0,0], 0, 15),
])
def test_numSubarraysWithSum(test_input1, test_input2, excepted_output):
    assert Sol0930().numSubarraysWithSum(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.todo
@pytest.mark.parametrize("test_input, excepted_output", [
    ("tree", "eert"),
    ("cccaaa", "aaaccc"),
    ("Aabb", "bbAa"),
])
def test_frequencySort(test_input, excepted_output):
    assert Sol0451().frequencySort(test_input) == excepted_output
    

@pytest.mark.todo
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ("cba", "abcd", "cbad"),  
  ("cbafg", "abcd", "cbad"),
])
def test_customSortString(test_input1, test_input2, excepted_output):
    assert Sol0791().customSortString(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.todo
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ("abc", "bca", True),  
  ("a", "aa", False),
  ("cabbba", "abbccc", True),
])
def test_closeStrings(test_input1, test_input2, excepted_output):
    assert Sol1657().closeStrings(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.todo
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ("abc", "bca", True),  
  ("a", "aa", False),
  ("cabbba", "abbccc", True),
])
def test_closeStrings(test_input1, test_input2, excepted_output):
    assert Sol1657().closeStrings(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.todo
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
  ("ab", "eidbaooo", True),  
  ("ab", "eidboaoo", False),
])
def test_checkInclusion(test_input1, test_input2, excepted_output):
    assert Sol1657().checkInclusion(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.todo
@pytest.mark.parametrize("test_input, excepted_output", [
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8),
])
def test_maximumUniqueSubarray(test_input, excepted_output):
    assert Sol1695().maximumUniqueSubarray(test_input) == excepted_output