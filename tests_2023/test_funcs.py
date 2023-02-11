"""
pytest can use assert to check everything
unittests has assertEquals, assertNotEquals, assertTrue, etc...

run test cases with:
py.test or 
pytest
python3 -m pytest
"""
import pytest

from tests_2023.mock_data import (
    render_test_nodes, 
    node_traversal, 
    m0713_test_array,
    m2270_test_nums
)

from LC_2023.e1480_RunningSumof1dArray import Solution as Sol1480
from LC_2023.e1672_richestCustomerWealth import Solution as Sol1672
from LC_2023.e0412_fizzBuzz import Solution as Sol0412
from LC_2023.e1342_NumberofStepsToReduceANumberToZero import Solution as Sol1342
from LC_2023.e0876_MiddleOfTheLinkedList import Solution as Sol0876
from LC_2023.e0383_Ranson_Note import Solution as Sol0383
from LC_2023.e0392_isSubsequence import Solution as Sol0392
from LC_2023.m0713_SubarrayProductLessThanK import Solution as Sol0713
from LC_2023.e0643_MaximumAverageSubarryI import Solution as Sol0643
from LC_2023.m1004_MaxConsecutiveOnesIII import Solution as Sol1004
from LC_2023.m2270_NumberOfWaysToSplitArray import Solution as Sol2270
from LC_2023.e1413_MinValueToGetPositiveStepByStepSum import Solution as Sol1413


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
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    *can_construct_comm_arg
])  
def test_canConstruct(test_input1, test_input2, excepted_output):
    assert Sol0383().canConstruct(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    *can_construct_comm_arg
])  
def test_canConstruct2(test_input1, test_input2, excepted_output):
    assert Sol0383().canConstruct2(test_input1, test_input2) == excepted_output
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False),
])    
def test_isSubsequence(test_input1, test_input2, excepted_output):
    assert Sol0392().isSubsequence(test_input1, test_input2) == excepted_output, "test failed"
    
   
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([10,5,2,6], 100, 8),
    ([1,2,3], 0, 0),
    (m0713_test_array, 815257, 30838731)
])     
def test_numSubarrayProductLessThanK(test_input1, test_input2, excepted_output):
    assert Sol0713().numSubarrayProductLessThanK(test_input1, test_input2) == excepted_output, "test failed"
    
    
@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([10,5,2,6], 100, 8),
    ([1,2,3], 0, 0),
    (m0713_test_array, 815257, 30838731)
])     
def test_numSubarrayProductLessThanK2(test_input1, test_input2, excepted_output):
    assert Sol0713().numSubarrayProductLessThanK2(test_input1, test_input2) == excepted_output, "test failed"
    

@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([1,12,-5,-6,50,3], 4, 12.75000),
    ([5], 1, 5.00000),
    ([0,4,0,3,2], 1, 4.00000)
])   
def test_findMaxAverage(test_input1, test_input2, excepted_output):
    assert Sol0643().findMaxAverage(test_input1, test_input2) == excepted_output
    

@pytest.mark.parametrize("test_input1, test_input2, excepted_output", [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),
])   
def test_longestOnes(test_input1, test_input2, excepted_output):
    assert Sol1004().longestOnes(test_input1, test_input2) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([2,3,1,0], 2),
    ([10,4,-8,7], 2),
    ([0, 0], 1),
    (m2270_test_nums, 99999)
])   
def test_waysToSplitArray(test_input1, excepted_output):
    assert Sol2270().waysToSplitArray(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([2,3,1,0], 2),
    ([10,4,-8,7], 2),
    ([0, 0], 1),
    (m2270_test_nums, 99999)
])   
def test_waysToSplitArray2(test_input1, excepted_output):
    assert Sol2270().waysToSplitArray2(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([2,3,1,0], 2),
    ([10,4,-8,7], 2),
    ([0, 0], 1),
    (m2270_test_nums, 99999)
])   
def test_waysToSplitArrayO1(test_input1, excepted_output):
    assert Sol2270().waysToSplitArrayO1(test_input1) == excepted_output
    
    
@pytest.mark.parametrize("test_input1, excepted_output", [
    ([-3, 2, -3, 4, 2], 5),
    ([1, 2], 1),
    ([1, -2, -3], 5),
    ([2,3,5,-5,-1], 1)
])   
def test_minStartValue(test_input1, excepted_output):
    assert Sol1413().minStartValue(test_input1) == excepted_output