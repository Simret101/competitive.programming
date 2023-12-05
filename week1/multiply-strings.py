class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        nums=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                mul=int(num1[i])*int(num2[j])
                pos1,pos2=i+j,i+j+1
                total=mul+nums[pos2]
                nums[pos1]+=total//10
                nums[pos2]=total%10
        res=""
        for i in nums:
            if res or i!=0:
                res+=str(i)
        return res if res else "0"
               