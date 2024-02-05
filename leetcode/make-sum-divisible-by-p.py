class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        target_remainder = sum(nums) % p
        if target_remainder == 0:
            return 0

        tot = 0
        dict = {0: -1}  
        min_length = float('inf')
        curr_remainder = 0

        for i, num in enumerate(nums):
            tot+= num
            curr_remainder = tot % p
            target = (curr_remainder - target_remainder) % p

            if target in dict:
                min_length = min(min_length, i - dict[target])

            dict[curr_remainder] = i

        return min_length if min_length < len(nums) else -1
        
