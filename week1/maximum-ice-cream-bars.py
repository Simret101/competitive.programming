class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        count=0
        res=0
        tot=0
        M=max(costs)
        arr=[0]*(M+1)
        for i in costs:
            arr[i]+=1
        for i in range(1,M+1):
            arr[i]+=arr[i-1]
        arr2=[0]*len(costs)
        for i in range(len(costs)-1,-1,-1):
            arr2[arr[costs[i]]-1]=costs[i]
            arr[costs[i]]-=1
        if arr2[0]>coins:
            return 0
        for i in range(len(arr2)):
            tot+=arr2[i]
            count+=1
            while tot>coins:
                tot-=arr2[i]
                count-=1

        return count     
    

       