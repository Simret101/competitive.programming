class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]   
        for i in range(len(firstList)): 
            j=0
            while j<len(secondList):
                x=max(firstList[i][0],secondList[j][0])
                y=min(firstList[i][1],secondList[j][1])
                if x<=y:
                    ans.append([x,y])
                j+=1
        return ans if ans else []