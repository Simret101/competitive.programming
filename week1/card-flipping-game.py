class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        count=0
        x=set()
        for front,back in zip(fronts,backs):
            if front==back:
                x.add(front)
    
        res=float('inf')
        for card in fronts + backs:
            if card not in x:
                res=min(card,res)
                 
        return res if res!=float('inf') else 0