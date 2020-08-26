class Heap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1]*self._maxsize
        self._csize = 0

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def insert(self, e):
        if self._csize == self._maxsize:
            print('Your Heap have reached it maximum Limit!')
            return
        
        self._csize = self._csize + 1
        h1 = self._csize

        # Up-heap bubbling
        while h1 > 1 and e > self._data[h1//2]:
            self._data[h1] = self._data[h1//2]
            h1 = h1//2
        
        self._data[h1] = e

    def deleteMax(self):
        if self._csize == 0:
            print('Your Heap is EMPTY!')
            return

        e = self._data[1]
        self._data[1] = self._data[self._csize]
        self._data[self._csize] = -1
        self._csize = self._csize - 1

        i = 1
        j = i*2
        while j <= self._csize:
            if self._data[j] < self._data[j+1]:
                j = j + 1
            if self._data[i] < self._data[j]:
                self._data[i], self._data[j] = self._data[j], self._data[i]

                i = j
                j = i*2
            else:
                break          
        return e      

    def max(self):
        if self._csize == 0:
            print('Your Heap is EMPTY!')
            return
        return self._data[1]

if __name__ == '__main__':
    heap = Heap()
    heap.insert(2)
    heap.insert(42)
    heap.insert(23)
    heap.insert(4)
    heap.insert(55)
    heap.insert(66)
    heap.insert(5)
    heap.insert(44)
    heap.insert(8)

    print(heap._data)

    heap.deleteMax()
    print(heap._data)