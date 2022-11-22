from __future__ import annotations
from typing import Iterable


class ListNode:
    def __init__(self, val: int = 0, nxt: ListNode = None):
        self.val = val
        self.nxt = nxt

    def _repr(self, nxt):
        if nxt is None:
            return ''

        rec_repr = self._repr(nxt=nxt.nxt)
        rec_repr = '' if len(rec_repr) == 0 else f'->{rec_repr}'

        return f'({nxt.val}){rec_repr}'

    def __repr__(self):
        return self._repr(self)

    def __eq__(self, other):
        return self.val == other.val and self.nxt == other.nxt


def build_list_node(vals: Iterable[int]) -> ListNode:
    if len(vals) == 0:
        return None

    sub_nodes = build_list_node(vals[1:])
    list_node = ListNode(vals[0], sub_nodes)

    return list_node