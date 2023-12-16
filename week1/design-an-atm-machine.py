class ATM(object):

    def __init__(self):
        self.store=[20,50,100,200,500]
        self.count=[0]*5
        

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(len(banknotesCount)):
            self.count[i] += banknotesCount[i]
    
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        ans=[0]*5
        tot=0
        for i in range(len(self.store)-1,-1,-1):
            prev=min(amount//self.store[i],self.count[i])
            ans[i]=prev
            tot+=prev*self.store[i]
            amount-=prev*self.store[i]      
        if amount!=0:
            return [-1]
        for i in range(len(self.store)):
            self.count[i]-=ans[i]
        return ans  


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)