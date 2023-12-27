class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        print(points)
        maxi=0
        for i in range(1,len(points)):
            ans=abs(points[i-1][0]-points[i][0])
            if ans>maxi:
                maxi=ans
        return maxi
        