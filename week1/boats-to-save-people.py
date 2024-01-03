class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boat=0
        l=0
        r=len(people)-1
        while l<=r:
            dif=limit-people[r]
            boat+=1
            r-=1
            if dif >=people[l]:
                l+=1
          
        return boat
        