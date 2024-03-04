
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=[]
        for i in range(len(costs)):
            tot=costs[i][0]-costs[i][1]
            ans.append([tot,costs[i][0],costs[i][1]])
        ans.sort()
        n=len(costs)
        tot=0
        for i in range (len(ans)):
            if i< (n//2):
                tot+=ans[i][1]
            else:
                tot+=ans[i][2]
        return tot

            
        
        
