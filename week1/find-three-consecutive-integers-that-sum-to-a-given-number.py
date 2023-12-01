class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3!=0:
            return []
        else:
            mid=num//3
            return [mid-1,mid,mid+1]
        
     
     
                  



