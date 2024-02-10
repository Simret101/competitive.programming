class Solution:
    def balancedString(self, s: str) -> int:
        char_indices = {'Q': 0, 'W': 1, 'E': 2, 'R': 3}
        chars = [0] * 4
        for c in s:
            chars[char_indices[c]] += 1
        
        target = len(s) // 4
        l = 0
        result = len(s)

        for r in range(len(s)):
            chars[char_indices[s[r]]] -= 1
            
            while (l < len(s) and chars[0] <= target and
                   chars[1] <= target and
                   chars[2] <= target and
                   chars[3] <= target):
                chars[char_indices[s[l]]] += 1
                result = min(result, r - l + 1)
                l += 1
        
        return result