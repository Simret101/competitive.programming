class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        prev=0
        for i in range(1,n+1):
            res=i%7
            if res%7==0:
                res+=7
            ans+=prev+res
            if i%7==0:
                prev+=1
        return ans  