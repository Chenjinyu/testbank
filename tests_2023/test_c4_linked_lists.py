import pytest

from data_structures_and_algorithms.c4_linked_lists.de0141_LinkedListCycle import Solution as Sol0141

@pytest.mark.parametrize("test_input1, excepted_output", [
    ([3,2,0,-4], True),
    ([1, 2], True),
    ([1], False),
])
def test_hasCycle(test_input1, excepted_output):
    assert Sol0141().hasCycle(test_input1) == excepted_output