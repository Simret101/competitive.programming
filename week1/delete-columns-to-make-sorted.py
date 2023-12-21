class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count=0
        n=len(strs)
        m=len(strs[0])
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j]=strs[j][i]
        res=[]
        for i in range(len(ans)):
            for j in range(len(ans[0])-1):
                if ans[i][j]>ans[i][j+1]:
                    count+=1
        
                    break
        return count
        
                    

        