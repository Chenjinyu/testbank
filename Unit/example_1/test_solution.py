import unittest
from typing import Iterable

from .list_node import build_list_node
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def _test_merge(self, vals_1: Iterable[int], vals_2: Iterable[int], vals_expected: Iterable[int]) -> None:
        l1 = build_list_node(vals_1)
        l2 = build_list_node(vals_2)

        merged = self.solution.merge_two_lists(l1, l2)

        expected = build_list_node(vals_expected)
        self.assertEqual(expected, merged)

    def test_same_size(self) -> None:
        vals_1, vals_2 = (1, 2, 4), (1, 3, 4)
        vals_expected = (1, 1, 2, 3, 4, 4)

        self._test_merge(vals_1, vals_2, vals_expected)

    def test_empty_empty(self) -> None:
        vals_1, vals_2 = (), ()
        vals_expected = ()

        self._test_merge(vals_1, vals_2, vals_expected)

    def test_empty_zero(self) -> None:
        vals_1, vals_2 = (), (0,)
        vals_expected = (0,)

        self._test_merge(vals_1, vals_2, vals_expected)


if __name__ == '__main__':
    unittest.main()