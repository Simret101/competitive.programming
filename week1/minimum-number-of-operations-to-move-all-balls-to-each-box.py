class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
       
        res=[]
        for i in range(len(boxes)):
            count=0
            for left in range(i-1,-1,-1):
                if boxes[left]=="1":
                    count+=i-left
            for right in range(i+1,len(boxes)):
                if boxes[right]=="1":
                    count+=right-i
            res.append(count)
        return res

            

        