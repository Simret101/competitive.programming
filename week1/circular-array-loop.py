class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited=set()
        for i in range(len(nums)):
            if i not in visited:
                visited_cycle=set()
                while True:
                    if i in visited_cycle:
                        return True
                    visited.add(i)
                    visited_cycle.add(i)
                    previous=i
                    i=(i+nums[i])%len(nums)
                    
                    if previous==i:
                        break
                    if nums[previous]>0 != nums[i]<0:
                        
                        break
        return False

        