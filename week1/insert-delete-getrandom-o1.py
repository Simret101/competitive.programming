class RandomizedSet(object):

    def __init__(self):
        self.randomize=set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.randomize:
            self.randomize.add(val)
            return True
        else:
            return False
        
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomize:
            self.randomize.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        if self.randomize:
            random_list = list(self.randomize)
            return random.choice(random_list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()