class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        
        total= sum(cardPoints)
        
        size = n - k
        max_score = 0
        
        tot = sum(cardPoints[:size])
        
        i = 0
        while i + size <= n:
            if i > 0:
                tot -= cardPoints[i-1]
                tot += cardPoints[i+size-1]
            max_score = max(max_score, total - tot)
            i += 1
        
        return max_score

        