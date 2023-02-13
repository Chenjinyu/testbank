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
    