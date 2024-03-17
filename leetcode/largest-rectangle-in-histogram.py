class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        next = [len(heights)] * len(heights)
        prev = [-1] * len(heights)
        stack = []

    
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                stackTop = stack.pop()
                next[stackTop] = i
            if stack:
                prev[i] = stack[-1]
            stack.append(i)

        maxA = 0
        for i in range(len(heights)):
            currentHeight = heights[i]
            width = next[i] - prev[i] - 1
            maxA = max(maxA, currentHeight * width)

        return maxA