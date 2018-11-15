[![HitCount](http://hits.dwyl.io/aayushuppal/bhpq.svg)](http://hits.dwyl.io/aayushuppal/bhpq)
[![GitHub contributors](https://img.shields.io/github/contributors/aayushuppal/bhpq.svg)](https://github.com/aayushuppal/bhpq/graphs/contributors)
[![version](https://img.shields.io/pypi/v/bhpq.svg)](https://pypi.python.org/pypi/bhpq)
[![license](https://img.shields.io/pypi/l/bhpq.svg)](https://pypi.python.org/pypi/bhpq)
[![Build Status](https://travis-ci.org/aayushuppal/bhpq.svg?branch=master)](https://travis-ci.org/aayushuppal/bhpq)

# BHPQ - Binary Heap Priority Queue

A binary heap priority queue implementation

## Installation

You can install bhpq from [PyPI](https://pypi.org/project/bhpq):

    pip install bhpq

bhpq is supported on Python 2.7, as well as Python 3.4 and above.

## Usage

    from bhpq import BinaryHeapPriorityQueue
    
    # The BinaryHeapPriorityQueue constructor takes two input params:
    
    # - prefer (required param)
    #    the preferred object is pushed to the top of the queue
    # the prefer input is a lambda function eg:
    # prefer=(lambda lhs, rhs: lhs if lhs.val >= rhs.val else rhs)
        
    # - size
    #    The size of the queue, default value is 10

## Example

    class Node(object):
    def __init__(self, val):
        self.val = val

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
    assert None == A.pop()

## Methods

- `size()`

returns the current size of the priority queue

- `peek()`

returns the object at the topof the priority queue if it exists else returns None

- `pop()`

removes and returns the object at the top of the priority queue if it exists else returns None

- `add(val)`

adds an element to the priority queue

## Maintainer

ⓘ [Aayush Uppal](https://aayushuppal.github.io)
