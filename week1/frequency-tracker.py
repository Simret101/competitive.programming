class FrequencyTracker(object):

    def __init__(self):
        self.frequency_tracker=defaultdict(int)
        self.freq=defaultdict(int)
        

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.frequency_tracker[number]+=1
        num=self.frequency_tracker[number]
        self.freq[num]+=1
        self.freq[num-1]-=1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency_tracker[number]>0:
            self.frequency_tracker[number]-=1
            num=self.frequency_tracker[number]
            self.freq[num]+=1
            self.freq[num+1]-=1
      


        # once=[]
      
        # for i in self.frequency_tracker:
        #     if self.frequency_tracker[i]==1:
        #         once.append(i)
        # for i in once:
        #     self.frequency_tracker.pop(i)
                

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return self.freq[frequency]>0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)