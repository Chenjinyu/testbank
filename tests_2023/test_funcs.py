"""
pytest can use assert to check everything
unittests has assertEquals, assertNotEquals, assertTrue, etc...

run test cases with:
py.test or 
pytest
python3 -m pytest

# Test marked as current_test test cases
pytest -m current_test


To show durations < 10 and these detail durations
`pytest --durations=10 --durations-min=1.0 -vv`

example output:
pytest --durations=10 --durations-min=1.0 -vv                                                                       *[master] 
======================================================================== test session starts ========================================================================
platform darwin -- Python 3.11.0, pytest-7.2.1, pluggy-1.0.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/jinyuchen/CodeCracking/testbank, configfile: pytest.ini
collected 48 items                                                                                                                                                  

test_funcs.py::test_runningsum1480[test_input0-excepted_output0] PASSED                                                                                       [  2%]
test_funcs.py::test_richestCus[test_input0-6] PASSED                                                                                                          [  4%]
test_funcs.py::test_richestCus[test_input1-17] PASSED                                                                                                         [  6%]
test_funcs.py::test_fizzBuzz2[15-excepted_output0] PASSED                                                                                                     [  8%]
test_funcs.py::test_fizzBuzz2[5-excepted_output1] PASSED                                                                                                      [ 10%]
test_funcs.py::test_fizzBuzz2[3-excepted_output2] PASSED                                                                                                      [ 12%]
test_funcs.py::test_numberOfSteps[14-6] PASSED                                                                                                                [ 14%]
test_funcs.py::test_numberOfSteps[8-4] PASSED                                                                                                                 [ 16%]
test_funcs.py::test_numberOfSteps[123-12] PASSED                                                                                                              [ 18%]
test_funcs.py::test_middleNode[test_input0-excepted_output0] PASSED                                                                                           [ 20%]
test_funcs.py::test_middleNode[test_input1-excepted_output1] PASSED                                                                                           [ 22%]
test_funcs.py::test_canConstruct[aa-aab-True] PASSED                                                                                                          [ 25%]
test_funcs.py::test_canConstruct[aab-aab-True] PASSED                                                                                                         [ 27%]
test_funcs.py::test_canConstruct[baa-aab-True] PASSED                                                                                                         [ 29%]
test_funcs.py::test_canConstruct[a-b-False] PASSED                                                                                                            [ 31%]
test_funcs.py::test_canConstruct2[aa-aab-True] PASSED                                                                                                         [ 33%]
test_funcs.py::test_canConstruct2[aab-aab-True] PASSED                                                                                                        [ 35%]
test_funcs.py::test_canConstruct2[baa-aab-True] PASSED                                                                                                        [ 37%]
test_funcs.py::test_canConstruct2[a-b-False] PASSED                                                                                                           [ 39%]
test_funcs.py::test_isSubsequence[abc-ahbgdc-True] PASSED                                                                                                     [ 41%]
test_funcs.py::test_isSubsequence[axc-ahbgdc-False] PASSED                                                                                                    [ 43%]
test_funcs.py::test_numSubarrayProductLessThanK[test_input10-100-8] PASSED                                                                                    [ 45%]
test_funcs.py::test_numSubarrayProductLessThanK[test_input11-0-0] PASSED                                                                                      [ 47%]
test_funcs.py::test_numSubarrayProductLessThanK[test_input12-815257-30838731] PASSED                                                                          [ 50%]
test_funcs.py::test_numSubarrayProductLessThanK2[test_input10-100-8] PASSED                                                                                   [ 52%]
test_funcs.py::test_numSubarrayProductLessThanK2[test_input11-0-0] PASSED                                                                                     [ 54%]
test_funcs.py::test_numSubarrayProductLessThanK2[test_input12-815257-30838731] PASSED                                                                         [ 56%]
test_funcs.py::test_findMaxAverage[test_input10-4-12.75] PASSED                                                                                               [ 58%]
test_funcs.py::test_findMaxAverage[test_input11-1-5.0] PASSED                                                                                                 [ 60%]
test_funcs.py::test_findMaxAverage[test_input12-1-4.0] PASSED                                                                                                 [ 62%]
test_funcs.py::test_longestOnes[test_input10-2-6] PASSED                                                                                                      [ 64%]
test_funcs.py::test_longestOnes[test_input11-3-10] PASSED                                                                                                     [ 66%]
test_funcs.py::test_waysToSplitArray[test_input10-2] PASSED                                                                                                   [ 68%]
test_funcs.py::test_waysToSplitArray[test_input11-2] PASSED                                                                                                   [ 70%]
test_funcs.py::test_waysToSplitArray[test_input12-1] PASSED                                                                                                   [ 72%]
test_funcs.py::test_waysToSplitArray[test_input13-99999] PASSED                                                                                               [ 75%]
test_funcs.py::test_waysToSplitArray2[test_input10-2] PASSED                                                                                                  [ 77%]
test_funcs.py::test_waysToSplitArray2[test_input11-2] PASSED                                                                                                  [ 79%]
test_funcs.py::test_waysToSplitArray2[test_input12-1] PASSED                                                                                                  [ 81%]
test_funcs.py::test_waysToSplitArray2[test_input13-99999] PASSED                                                                                              [ 83%]
test_funcs.py::test_waysToSplitArrayO1[test_input10-2] PASSED                                                                                                 [ 85%]
test_funcs.py::test_waysToSplitArrayO1[test_input11-2] PASSED                                                                                                 [ 87%]
test_funcs.py::test_waysToSplitArrayO1[test_input12-1] PASSED                                                                                                 [ 89%]
test_funcs.py::test_waysToSplitArrayO1[test_input13-99999] PASSED                                                                                             [ 91%]
test_funcs.py::test_minStartValue[test_input10-5] PASSED                                                                                                      [ 93%]
test_funcs.py::test_minStartValue[test_input11-1] PASSED                                                                                                      [ 95%]
test_funcs.py::test_minStartValue[test_input12-5] PASSED                                                                                                      [ 97%]
test_funcs.py::test_minStartValue[test_input13-1] PASSED                                                                                                      [100%]

======================================================================= slowest 10 durations ========================================================================
3.47s call     tests_2023/test_funcs.py::test_numSubarrayProductLessThanK[test_input12-815257-30838731]
2.12s call     tests_2023/test_funcs.py::test_waysToSplitArray[test_input13-99999]
0.02s call     tests_2023/test_funcs.py::test_waysToSplitArray2[test_input13-99999]
0.01s call     tests_2023/test_funcs.py::test_waysToSplitArrayO1[test_input13-99999]
0.00s call     tests_2023/test_funcs.py::test_numSubarrayProductLessThanK2[test_input12-815257-30838731]
0.00s setup    tests_2023/test_funcs.py::test_waysToSplitArrayO1[test_input13-99999]
0.00s setup    tests_2023/test_funcs.py::test_runningsum1480[test_input0-excepted_output0]
0.00s setup    tests_2023/test_funcs.py::test_waysToSplitArrayO1[test_input12-1]
0.00s setup    tests_2023/test_funcs.py::test_isSubsequence[axc-ahbgdc-False]
0.00s setup    tests_2023/test_funcs.py::test_numSubarrayProductLessThanK[test_input11-0-0]
======================================================================== 48 passed in 5.71s =========================================================================
"""
import pytest

from tests_2023.mock_data import (
    render_test_nodes, 
    node_traversal, 
    m0713_test_array,
    m2270_test_nums
)

from lc_2023.e1480_RunningSumof1dArray import Solution as Sol1480
from lc_2023.e1672_richestCustomerWealth import Solution as Sol1672
from lc_2023.e0412_fizzBuzz import Solution as Sol0412
from lc_2023.e1342_NumberofStepsToReduceANumberToZero import Solution as Sol1342
from lc_2023.e0876_MiddleOfTheLinkedList import Solution as Sol0876

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
from data_structures_and_algorithms.c2_arrays_and_strings.m1208_GetEqualSubstringsWithinBudget import Solution as Sol1228
from data_structures_and_algorithms.c2_arrays_and_strings.e1732_FindTheHighestAltitude import Solution as Sol1732
from data_structures_and_algorithms.c2_arrays_and_strings.e0724_FindPivotIndex import Solution as Sol0724
from data_structures_and_algorithms.c2_arrays_and_strings.e0303_RangeSumQuery_Immutable import Solution as Sol0303

@pytest.mark.parametrize("test_input, excepted_output", [([3,1,2,10,1], [3,4,6,16,17])])    
def test_runningsum1480(test_input, excepted_output):
    assert Sol1480().runningSum2(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [([[1,2,3],[3,2,1]], 6), ([[2,8,7],[7,1,3],[1,9,5]], 17)])  
def test_richestCus(test_input, excepted_output):
    assert Sol1672().maximumWealth(test_input) == excepted_output
  
   
@pytest.mark.parametrize("test_input, excepted_output", [
    (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]), 
    (5, ["1","2","Fizz","4","Buzz"]),
    (3, ["1","2","Fizz"])
])     
def test_fizzBuzz2(test_input, excepted_output):
    assert Sol0412().fizzBuzz2(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [
    (14, 6), (8, 4), (123, 12)
])  
def test_numberOfSteps(test_input, excepted_output):
    assert Sol1342().numberOfSteps(test_input) == excepted_output
    
    
@pytest.mark.parametrize("test_input, excepted_output", [
    (
        render_test_nodes([1,2,3,4,5]), [3,4,5]
    ),(
        render_test_nodes([1,2,3,4,5,6]), [4,5, 6]
    )
])
def test_middleNode(test_input, excepted_output):
    assert node_traversal(Sol0876().middleNode(test_input)) == excepted_output
    
    
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
@pytest.mark.current_test
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ("abcdefd", "d", "dcbaefd"),
    ("xyxzxe", "z", "zxyxxe"),
    ("abcd", "z", "abcd")
])    
def test_moveZeroes(test_input1, test_input2, excepted_output):
    assert Sol2000().reversePrefix(test_input1, test_input2) == excepted_output