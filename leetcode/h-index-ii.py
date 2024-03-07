class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        l=0
        r=len(citations)
        def helper(mid):
            for i in range(mid):
                if citations[i]<mid:
                    return False
            return True
       
        # if len(citations)==1 and citations[0]!=0:
        #     return 1
        # elif len(citations)==1 and citations[0]==0:
        #     return 0

        while l<=r:
            mid=(l+r)//2
            
            
            if helper(mid):

                l=mid+1
                
                
                
                      
            else:
               r=mid-1
                
                
        return r
                
        
        #     if citations[len(citations)-1] - citations[mid]==(len(citations)-1)-mid:
        #         return mid
        #     elif citations[len(citations)-1] - citations[mid]>(len(citations)-1)-mid:
        #         l=mid+1
                
        #     else:
        #         r=mid-1
        # return r
        