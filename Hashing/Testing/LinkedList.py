class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next = None):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def isempty(self):
        return self._size == 0  

    def insertsorted(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            p = self._head
            q = self._head
            while p and p._element < e:
                q = p
                p = p._next
            if p == self._head:
                newest._next = self._head
                self._head = newest
            else:
                newest._next = q._next
                q._next = newest
        self._size += 1

    def search(self, key):
        p = self._head
        index = 0

        while p:
            if p == key:
                return index
            p = p._next
            index += 1
        return -1

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

