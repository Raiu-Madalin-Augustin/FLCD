class HashTable:
    def __init__(self, size):

        self.size = size
        self.table = []

        for index in range(size):
            self.table.append([])

    def getSize(self):
        return self.size

    def __hash(self, key):
        sum = 0
        for char in str(key):
            sum += ord(char.lower())
        return sum % self.size

    def add(self, key):
        hashValue = self.__hash(key)
        if key not in self.table[hashValue]:
            self.table[hashValue].append(key)

    def remove(self, key):
        hashvalue = self.__hash(key)
        if key in self.table[hashvalue]:
            self.table[hashvalue].remove(key)

    def contains(self, key):
        hashValue = self.__hash(key)
        return key in self.table[hashValue]

    def getIndex(self,value):
        key = self.__hash(value)
        return self.table[key].index(value)
    def __str__(self):
        string = ""
        hashValue = 0
        for i in self.table:
            for keyword in i:
                string = string + "(" + str(hashValue) + "," + str(self.getIndex(keyword)) + ") : " + str(keyword) + "\n"
            hashValue += 1
            string = string + "\n"

        return string


