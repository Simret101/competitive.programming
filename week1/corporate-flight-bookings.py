class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+2)
        for start,end,val in bookings:
            ans[start]+=val
            ans[end+1]-=val 
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]
        return ans[1:-1]