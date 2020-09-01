class LinearProbing:
    def __init__(self):
        self.hashtable_size= 10
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key):
        return key % self.hashtable_size

    def lprobe(self, element):
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != 0:
            j += 1
        return (i+j) % self.hashtable_size

    def insert(self, element):
        i = self.lprobe(element)
        self.hashtable[i] = element

    def display(self):
        return self.hashtable

    def search(self, key):
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i+j) % self.hashtable_size] != key:
            if self.hashtable[(i+j) % self.hashtable_size] == 0:
                return False
            j += 1
        return True
        
if __name__ == '__main__':
    H = LinearProbing()

    H.insert(54)
    H.insert(78)
    H.insert(64)
    H.insert(92)
    H.insert(34)
    H.insert(86)
    H.insert(28)

    print(H.display())

    print('Searching:', H.search(55))
    print('Searching:', H.search(86))