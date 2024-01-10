class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        if k>len(blocks):return 0
        l,r=0,0
        count=0
        res=len(blocks)+1
        while r<len(blocks):
            if blocks[r]=="W":
                count+=1
            if r-l+1>=k:
                res=min(res,count)
                if blocks[l]=="W":
                    count-=1
                l+=1
            r+=1
    
        return res
    

       