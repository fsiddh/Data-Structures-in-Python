from LinkedList import LinkedList

class HashChain:
    def __init__(self):
        self._hashtable_size = 10
        self.hashtable = [0] * self._hashtable_size

if __name__ == '__main__':
    hchain = HashChain()
    print(hchain.hashtable)