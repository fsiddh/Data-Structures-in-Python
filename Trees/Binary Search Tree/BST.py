from queueslinked import QueuesLinked


class _Node:
    __slot__ = '_element', '_left', '_right'
    
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def insert(self, troot, e):
        temp = None

        while troot:
            temp = troot
            if e == troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n    
    
    def rinsert(self, troot, e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left, e)
            else:
                troot._right = self.rinsert(troot._right, e)
        else:
            n = _Node(e)
            troot = n
        return troot
    
    def search(self, key):
        troot = self._root
        
        while troot:
            if key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
            else:
                return True
        return False

    def rsearch(self, troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.rsearch(troot._left, key)
            elif key > troot._element:
                return self.rsearch(troot._right, key)
        else:
            return False
       
    def rinorder(self, troot):
        if troot:
            self.rinorder(troot._left)
            print(troot._element)
            self.rinorder(troot._right)

    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x+y+1
        return 0

    def height(self, troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)

            if x > y:
                return x + 1
            else:
                return y + 1
        return -1

    def levelorder(self):
        q = QueuesLinked()
        t = self._root

        q.enqueue(t)

        while not q.isempty():
            t = q.dequeue()
            print(t._element)
            if t._left:
                q.enqueue(t._left)
            if t._right:
                q.enqueue(t._right)

B = BinarySearchTree()
B.insert(B._root, 40)
B.insert(B._root, 80)
B.insert(B._root, 20)
B.insert(B._root, 90)
B.insert(B._root, 60)

B.rinsert(B._root, 30)

B.rinorder(B._root)

# False Conditions
print(B.search(35))

# True Condition
print(B.search(90))

# Recurssive Search
print(B.rsearch(B._root, 8))

# Count no. of Nodes
print(B.count(B._root))

# Height of the tree
print(B.height(B._root))

# Level Order Traversal
B.levelorder()