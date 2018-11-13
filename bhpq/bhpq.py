"""Binary Heap Priority Queue

Usage:
------

    $ from bhpq import BinaryHeapPriorityQueue

Contact:
--------

- https://aayushuppal.github.io

More information is available at:

- https://pypi.org/project/bhpq
- https://github.com/aayushuppal/bhpq

"""


class BinaryHeapPriorityQueue(object):
    def __init__(self, prefer, size=10):
        self._heapList = [None for i in range(0, size + 1)]
        self._currentSize = 0
        self._prefer = prefer
        return

    def size(self):
        return self._currentSize

    def peek(self):
        result = self._heapList[1] if self._currentSize >= 1 else None
        return result

    def pop(self):
        if self._currentSize < 1:
            return None
        result = self._heapList[1]
        self.__exch(1, self._currentSize)
        self._heapList[self._currentSize] = None
        self._currentSize -= 1
        self.__sink(1)
        return result

    def add(self, val):
        MAX_HEAPLIST_INDEX = len(self._heapList) - 1
        VAL_INDEX = self._currentSize + 1

        if VAL_INDEX > MAX_HEAPLIST_INDEX:
            self._heapList.append(val)
        else:
            self._heapList[VAL_INDEX] = val

        self._currentSize += 1
        self.__swim(self._currentSize)
        return

    def __sink(self, n):
        k = n
        while 2 * k <= self._currentSize:
            j = 2 * k
            if j < self._currentSize and self._heapList[j + 1] == self._prefer(
                self._heapList[j], self._heapList[j + 1]
            ):
                j += 1
            if self._heapList[k] == self._prefer(self._heapList[j], self._heapList[k]):
                break
            self.__exch(j, k)
            k = j
        return

    def __swim(self, n):
        k = n
        while (k > 1) and self._heapList[k] == self._prefer(
            self._heapList[k], self._heapList[int(k / 2)]
        ):
            self.__exch(k, int(k / 2))
            k = int(k / 2)
        return

    def __exch(self, i, j):
        temp = self._heapList[i]
        self._heapList[i] = self._heapList[j]
        self._heapList[j] = temp
        return
