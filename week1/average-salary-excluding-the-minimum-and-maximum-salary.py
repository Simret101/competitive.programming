class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        size=float(len(salary)-2)
   
        salary.sort()
        return (sum(salary)- salary[0]- salary[-1]) / size
      
    