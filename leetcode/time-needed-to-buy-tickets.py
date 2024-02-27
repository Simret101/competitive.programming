class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        ans=0
        
        for i in range(len(tickets)):
            q.append(i)
        while len(q)!=0:
            x=q.popleft()
            if tickets[x]!=0:
                q.append(x)
                tickets[x]-=1
                
                ans+=1

                if tickets[x]==0 and x==k:
                    return  ans
        return ans
        

        
        
            
           
            
      
           