class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        count_forward = {}
        count_backward = {}

        for i in range(len(nums)):
            if nums[i] in count_forward:
                result[i] += count_forward[nums[i]][0] * i - count_forward[nums[i]][1]
                count_forward[nums[i]][0] += 1
                count_forward[nums[i]][1] += i
            else:
                count_forward[nums[i]] = [1, i]

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in count_backward:
                result[i] += count_backward[nums[i]][1] - count_backward[nums[i]][0] * i
                count_backward[nums[i]][0] += 1
                count_backward[nums[i]][1] += i
            else:
                count_backward[nums[i]] = [1, i]

        return result


