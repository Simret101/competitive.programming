class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        points.sort()
        ans=[points[0]]
        for i in range(1,len(points)):
            if points[i][0]<=ans[-1][1]:
                ans[-1][1]=min(points[i][1],ans[-1][1])
            elif points[i][0]>ans[-1][1]:
                ans.append(points[i])
        return len(ans)

