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
