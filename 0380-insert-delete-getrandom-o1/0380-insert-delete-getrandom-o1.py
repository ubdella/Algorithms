class RandomizedSet:

    def __init__(self):
        self.stackVals = []
        self.indices = {}        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.stackVals.append(val)
        self.indices[val] = len(self.stackVals) - 1 
        return True      

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        lastVal = self.stackVals[-1]
        lastValIndex = len(self.stackVals) - 1
        valIndex = self.indices[val]
        self.stackVals[valIndex] = lastVal
        self.stackVals[lastValIndex] = val
        self.indices[lastVal] = valIndex
        del self.indices[val]
        self.stackVals.pop()

        return True       

    def getRandom(self) -> int:
        return random.choice(self.stackVals)      


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()