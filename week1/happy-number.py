class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_digit(num):
            tot_digit=0
            while num>0:
                digit=num%10
                num=num//10
                tot_digit+=digit**2
            return tot_digit
        slow=n
        fast=sum_digit(n)
        while fast!=1 and slow!=fast:
            slow=sum_digit(slow)
            fast=sum_digit(sum_digit(fast))
        if fast==1:
            return True
        else:
            return False