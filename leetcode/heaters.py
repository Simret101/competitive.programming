class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = -1
        right = max(max(houses), max(heaters))
        print(right)
        def helper(mid):
            i = 0
            j = 0
          
            while i < len(houses) and j < len(heaters):

                if (heaters[j] - mid) > houses[i]:
                    return  False
                if (heaters[j] + mid) < houses[i]:
                    j += 1
                else:
                    i += 1
            if i>= len(houses):
                return True
            return False

        while left+1 < right:
            mid = (left + right) // 2

            if helper(mid):
                right = mid
            else:
                left = mid
        return right
        
        # def helper(mid):
        #     i,j=0,0
            
        #     while i<len(houses) and j<len(heaters):
        #         if heaters[j]-mid<houses[i]:
        #             return False
                
                                                                                 

        #     while l<=r:
        #         l=0
        #         r=len(heaters)
        #         mid=(l+r)//2
        #         if mid>houses[i] :
        #             r=mid-1
        #         else:
        #             l=mid+1
        #     return l

        #     for i in heaters:
        #         max_val=max(max_val,mid+i)
        #         ans=i-mid

        #         if ans < min(houses):
        #            ans=min(houses)
        #         min_val=min(min_val,mid-i)
        #         return(min(houses)==min_val and max(houses)<=max_val)
        # ans=max(ans,x)
        # for i in range(len(houses)):
            
        #     l=0
        #     r=max(heaters)
           
        #     while l<=r:
        #         l=0
        #         r=len(heaters)
        #         mid=(l+r)//2
        #         if mid>houses[i] :
        #             r=mid-1
        #         else:
        #             l=mid+1
        #     return l
        #     x=min(houses[i]-heaters[l],houses[i]-heaters[l-1])
        #     if houses[0]==heaters[0]:
        #         return 


                
