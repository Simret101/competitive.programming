class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        mod = 10**9 + 7
        n = len(nums)
        
        def helper(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        
        for i in range(n):
            j = helper(nums, target - nums[i]) - 1
            if j >= i:
                count += pow(2, j - i, mod)
        
        return count % mod