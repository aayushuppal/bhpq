"""Tests for the bhpq.bhpq module"""

import pytest
from bhpq import BinaryHeapPriorityQueue


class Node(object):
    def __init__(self, val):
        self.val = val


#
# Tests
#
def test_node1():

    A = BinaryHeapPriorityQueue(
        prefer=(lambda lhs, rhs: lhs if lhs.val >= rhs.val else rhs), size=5
    )
    A.add(Node(1))
    A.add(Node(4))
    A.add(Node(3))
    A.add(Node(5))
    A.add(Node(2))

    assert 5 == A.pop().val
    assert 4 == A.pop().val
    assert 3 == A.pop().val
    assert 2 == A.pop().val
    assert 1 == A.pop().val


def test_node2():

    A = BinaryHeapPriorityQueue(
        prefer=(lambda lhs, rhs: lhs if lhs.val <= rhs.val else rhs), size=3
    )
    A.add(Node(1))
    A.add(Node(4))
    A.add(Node(3))

    assert 1 == A.pop().val
    assert 3 == A.pop().val
    assert 4 == A.pop().val


def test_val1():

    A = BinaryHeapPriorityQueue(
        prefer=(lambda lhs, rhs: lhs if lhs >= rhs else rhs), size=3
    )
    A.add(1)
    A.add(3)
    A.add(2)

    assert 3 == A.pop()
    assert 2 == A.pop()
    assert 1 == A.pop()
    assert None == A.pop()
    assert 0 == A.size()
