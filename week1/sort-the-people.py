class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        sorted_height=sorted(heights,reverse=True)
        res=[]
        for i in sorted_height:
            res.append(names[heights.index(i)])
        return res

      
        