class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        l=0
        r=0
        res=len(cards)+1
        store=set()
        while r<len(cards):   
            while cards[r] in store:
                store.remove(cards[l]) 
                res=min(res,r-l+1)
                l+=1        
            
            store.add(cards[r])
            r+=1
        return -1 if res==len(cards)+1 else res
        
        
    