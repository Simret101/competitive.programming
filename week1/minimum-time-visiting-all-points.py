class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        second_count=0
        for i in range(1,len(points)):
            x1,y1=points[i]
            x2,y2=points[i-1]
            second_count+=max(abs(x2-x1),abs(y2-y1))
        return second_count
    
        

        

        