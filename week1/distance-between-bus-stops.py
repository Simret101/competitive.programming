class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start>destination:
            start,destination=destination,start
        tot=sum(distance)
        cur_sum=sum(distance[start:destination])
        return min(cur_sum,tot-cur_sum)