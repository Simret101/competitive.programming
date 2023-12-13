class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.dict1=defaultdict(list)
        self.ptr=1
        
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.dict1[idKey].append(value)
        
       
        result = []
        while self.ptr in self.dict1:
            result.extend(self.dict1[self.ptr])
            self.ptr += 1
        
        return result

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)