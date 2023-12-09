class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for x in nums:
            if x>0:
                pos.append(x)
            else:
                neg.append(x)
        res=[]
        p,n=0,0
        while p<len(pos) and n<len(neg):
            res.append(pos[p])
            res.append(neg[n])
            p+=1
            n+=1
        return res

        