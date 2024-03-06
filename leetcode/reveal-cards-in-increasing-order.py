
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        q = deque()
        for i in deck:
            if q:
                q.appendleft(q.pop())
                
            q.appendleft(i)
        return q

        
            

