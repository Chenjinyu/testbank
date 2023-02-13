import pytest

from tests_2023.mock_data import (
    render_test_nodes, 
    node_traversal, 
    m0713_test_array,
    m2270_test_nums
)

from data_structures_and_algorithms.c3_hashing.e0001_TwoSum import Solution as Sol0001
from data_structures_and_algorithms.c3_hashing.e2351_FirstLetterToAppearTwice import Solution as Sol2351


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