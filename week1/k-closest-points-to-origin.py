class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            distances.append(distance)

        pairs = zip(distances, points)
        sorted_pairs = sorted(pairs)
        sorted_points = []
        for _, point in sorted_pairs:
            sorted_points.append(point)
        k_closest_points = sorted_points[:k]
        return k_closest_points


        