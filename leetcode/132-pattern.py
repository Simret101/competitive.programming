class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ans = [0] * len(nums)
        stack = []

        for i in range(len(nums)):
            if i == 0:
                ans[i] = 0
            else:
                if nums[i] < nums[ans[i - 1]]:
                    ans[i] = i
                else:
                    ans[i] = ans[i - 1]

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                if nums[ans[stack[-1]]] < nums[i]:
                    return True

            stack.append(i)

        return False