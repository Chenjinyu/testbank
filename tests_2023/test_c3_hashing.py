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