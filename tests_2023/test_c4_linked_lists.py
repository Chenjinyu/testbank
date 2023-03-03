import pytest

from data_structures_and_algorithms.c4_linked_lists.de0141_LinkedListCycle import Solution as Sol0141
from data_structures_and_algorithms.c4_linked_lists.e0876_MiddleOfTheLinkedList import Solution as Sol0876
from data_structures_and_algorithms.c4_linked_lists.e0083_RemoveDuplicatesFromSortedList import Solution as Sol0083

@pytest.mark.parametrize("test_input1, excepted_output", [
    ([3,2,0,-4], True),
    ([1, 2], True),
    ([1], False),
])
def test_hasCycle(test_input1, excepted_output):
    assert Sol0141().hasCycle(test_input1) == excepted_output
    
    
    
    
    