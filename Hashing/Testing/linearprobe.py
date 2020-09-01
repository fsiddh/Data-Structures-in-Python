class LinearProbing:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key):
        return key % self.hashtable_size

    def 