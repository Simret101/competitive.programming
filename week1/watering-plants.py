class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        res=0
        cur=capacity
        for i in range(len(plants)):
            if cur < plants[i]:
                res+=(i)*2+1
                cur=capacity
            else:
                res+=1
            cur-=plants[i]
        return res
            
