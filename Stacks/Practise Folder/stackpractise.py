class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next=None):
        self._element = element
        self._next = next


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def len(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
    
    def pop(self):
        if self.isempty():
            print('Your stack is empty')
            return 
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.isempty():
            print('Stack empty')
            return 
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end='-->')
            p = p._next
        print() 

if __name__ == '__main__':
    S = Stack()

    S.push(4)
    S.push(8)
    S.push(7)
    S.push(2)
    S.push(9)
    S.display()

    print(S.pop())
    S.display()
