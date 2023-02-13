"""
pytest can use assert to check everything
unittests has assertEquals, assertNotEquals, assertTrue, etc...

run test cases with:
*. py.test 
*. pytest
*. python3 -m pytest

Test with one test file:
*. pytest test_c2_array_and_strings.py
*. pytest test_c2_array_and_strings.py::test_canConstruct  -> (it will check rest of testcase if any issuse before running it.)
*. pytest test_c2_array_and_strings.py -m c2_arrays_and_strings 

# Test marked as current_test test cases
pytest -m current_test

To show durations < 10 and these detail durations
`pytest --durations=10 --durations-min=1.0 -vv`
"""
import pytest

from tests_2023.mock_data import (
    render_test_nodes, 
    node_traversal, 
    m0713_test_array,
    m2270_test_nums
)

from data_structures_and_algorithms.c2_arrays_and_strings.e0383_Ranson_Note import Solution as Sol0383
from data_structures_and_algorithms.c2_arrays_and_strings.e0392_isSubsequence import Solution as Sol0392
from data_structures_and_algorithms.c2_arrays_and_strings.m0713_SubarrayProductLessThanK import Solution as Sol0713
from data_structures_and_algorithms.c2_arrays_and_strings.e0643_MaximumAverageSubarryI import Solution as Sol0643
from data_structures_and_algorithms.c2_arrays_and_strings.m1004_MaxConsecutiveOnesIII import Solution as Sol1004
from data_structures_and_algorithms.c2_arrays_and_strings.m2270_NumberOfWaysToSplitArray import Solution as Sol2270
from data_structures_and_algorithms.c2_arrays_and_strings.e1413_MinValueToGetPositiveStepByStepSum import Solution as Sol1413
from data_structures_and_algorithms.c2_arrays_and_strings.e0557_ReverseWordsInAStringIII import Solution as Sol0557
from data_structures_and_algorithms.c2_arrays_and_strings.e0917_ReverseOnlyLetters import Solution as Sol0917
from data_structures_and_algorithms.c2_arrays_and_strings.e0283_MoveZeroes import Solution as Sol0283
from data_structures_and_algorithms.c2_arrays_and_strings.e2000_ReversePrefixOfWord import Solution as Sol2000
from data_structures_and_algorithms.c2_arrays_and_strings.m0209_MinimumSizeSubarraySum import Solution as Sol0209
from data_structures_and_algorithms.c2_arrays_and_strings.m1456_MaximumNumberofVowelsInASubstringOfGivenLength import Solution as Sol1456
from data_structures_and_algorithms.c2_arrays_and_strings.m1208_GetEqualSubstringsWithinBudget import Solution as Sol1208
from data_structures_and_algorithms.c2_arrays_and_strings.e1732_FindTheHighestAltitude import Solution as Sol1732
from data_structures_and_algorithms.c2_arrays_and_strings.e0724_FindPivotIndex import Solution as Sol0724
from data_structures_and_algorithms.c2_arrays_and_strings.e0303_RangeSumQuery_Immutable import NumArray

    

can_construct_comm_arg = (
    ('aa', 'aab', True),
    ('aab', 'aab', True),
    ('baa', 'aab', True),
    ('a', 'b', False),
)
@pytest.mark.c2_arrays_and_strings
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    *can_construct_comm_arg
])  
def test_canConstruct(test_input1, test_input2, excepted_output):
    assert Sol0383().canConstruct(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    *can_construct_comm_arg
])  
def test_canConstruct2(test_input1, test_input2, excepted_output):
    assert Sol0383().canConstruct2(test_input1, test_input2) == excepted_output


@pytest.mark.c2_arrays_and_strings
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False),
])    
def test_isSubsequence(test_input1, test_input2, excepted_output):
    assert Sol0392().isSubsequence(test_input1, test_input2) == excepted_output, "test failed"
    
    
@pytest.mark.c2_arrays_and_strings
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([10,5,2,6], 100, 8),
    ([1,2,3], 0, 0),
    (m0713_test_array, 815257, 30838731)
])     
def test_numSubarrayProductLessThanK(test_input1, test_input2, excepted_output):
    assert Sol0713().numSubarrayProductLessThanK(test_input1, test_input2) == excepted_output, "test failed"
   
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([10,5,2,6], 100, 8),
    ([1,2,3], 0, 0),
    (m0713_test_array, 815257, 30838731)
])     
def test_numSubarrayProductLessThanK2(test_input1, test_input2, excepted_output):
    assert Sol0713().numSubarrayProductLessThanK2(test_input1, test_input2) == excepted_output, "test failed"
    
    
@pytest.mark.c2_arrays_and_strings
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([1,12,-5,-6,50,3], 4, 12.75000),
    ([5], 1, 5.00000),
    ([0,4,0,3,2], 1, 4.00000)
])   
def test_findMaxAverage(test_input1, test_input2, excepted_output):
    assert Sol0643().findMaxAverage(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
])   
def test_longestOnes(test_input1, test_input2, excepted_output):
    assert Sol1004().longestOnes(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings
@pytest.mark.slow
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([2,3,1,0], 2),
    ([10,4,-8,7], 2),
    ([0, 0], 1),
    (m2270_test_nums, 99999)
])   
def test_waysToSplitArray(test_input1, excepted_output):
    assert Sol2270().waysToSplitArray(test_input1) == excepted_output
    

@pytest.mark.c2_arrays_and_strings
@pytest.mark.slow
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([2,3,1,0], 2),
    ([10,4,-8,7], 2),
    ([0, 0], 1),
    (m2270_test_nums, 99999)
])   
def test_waysToSplitArray2(test_input1, excepted_output):
    assert Sol2270().waysToSplitArray2(test_input1) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings
@pytest.mark.slow
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([2,3,1,0], 2),
    ([10,4,-8,7], 2),
    ([0, 0], 1),
    (m2270_test_nums, 99999)
])   
def test_waysToSplitArrayO1(test_input1, excepted_output):
    assert Sol2270().waysToSplitArrayO1(test_input1) == excepted_output
    
      
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([-3, 2, -3, 4, 2], 5),
    ([1, 2], 1),
    ([1, -2, -3], 5),
    ([2,3,5,-5,-1], 1)
])   
def test_minStartValue(test_input1, excepted_output):
    assert Sol1413().minStartValue(test_input1) == excepted_output
    

@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD"),
])   
def test_reverseWords(test_input1, excepted_output):
    assert Sol0557().reverseWords(test_input1) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD"),
])   
def test_reverseWordsSimple(test_input1, excepted_output):
    assert Sol0557().reserseWordsSimple(test_input1) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
])    
def test_reverseOnlyLetters(test_input1, excepted_output):
    assert Sol0917().reverseOnlyLetters(test_input1) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
])    
def test_reverseOnlyLettersWithSplitStr(test_input1, excepted_output):
    assert Sol0917().reverseOnlyLettersWithSplitStr(test_input1) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([0,0,1], [1,0,0])
])    
def test_moveZeroes(test_input1, excepted_output):
    assert Sol0283().moveZeroes(test_input1) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ("abcdefd", "d", "dcbaefd"),
    ("xyxzxe", "z", "zxyxxe"),
    ("abcd", "z", "abcd")
])    
def test_moveZeroes(test_input1, test_input2, excepted_output):
    assert Sol2000().reversePrefix(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.current_test
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    (7, [2,3,1,2,4,3], 2),
    (4, [1,4,4], 1),
    (11, [1,1,1,1,1,1,1,1], 0)
])    
def test_minSubArrayLen(test_input1, test_input2, excepted_output):
    assert Sol0209().minSubArrayLen(test_input1, test_input2) == excepted_output
    
    
# @pytest.mark.c2_arrays_and_strings 
# @pytest.mark.in_progress
# @pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
#     ("abciiidef", 3, 3),
#     ("aeiou", 2, 2),
#     ("leetcode", 3, 2)
# ])    
# def test_maxVowels(test_input1, test_input2, excepted_output):
#     assert Sol1456().maxVowels(test_input1, test_input2) == excepted_output
    
    
# @pytest.mark.c2_arrays_and_strings 
# @pytest.mark.in_progress
# @pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
#     ("abcd", "bcdf", 3),
#     ("abcd", "cdef", 3),
#     ("abcd", "acde", 0)
# ])    
# def test_equalSubstring(test_input1, test_input2, excepted_output):
#     assert Sol1208().equalSubstring(test_input1, test_input2) == excepted_output
    
    
# @pytest.mark.c2_arrays_and_strings 
# @pytest.mark.in_progress
# @pytest.mark.parametrize("test_input1, excepted_output", [
#     (["NumArray", "sumRange", "sumRange", "sumRange"][[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]], [None, 1, -1, -3]),
# ])    
# def test_sumRange(test_input1, excepted_output):
    # assert NumArray().sumRange(test_input1) == excepted_output
    
        
@pytest.mark.c2_arrays_and_strings 
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([-5,1,5,0,-7], 1),
    ([-4,-3,-2,-1,4,3,2], 0)
])    
def test_largestAltitude(test_input1, excepted_output):
    assert Sol1732().largestAltitude(test_input1) == excepted_output
    
    
# @pytest.mark.c2_arrays_and_strings 
# @pytest.mark.in_progress
# @pytest.mark.parametrize("test_input1, excepted_output", [
#     ([1,7,3,6,5,6], 3),
#     ([1,2,3], -1),
#     ([2,1,-1], 0)
# ])    
# def test_pivotIndex(test_input1, excepted_output):
    # assert Sol0724().pivotIndex(test_input1) == excepted_output