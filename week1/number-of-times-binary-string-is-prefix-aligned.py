class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        count=0
        arr=[0]*(len(flips))
        pre=[0]*(len(flips))
        #arr=[0 for _ in range(len(flips))]
        for i in range(len(flips)): 
            ans=flips[i]-1
            pre[i]=1
            if arr[ans]==0:
                arr[ans]=1
            else:
                arr[ans]=0

            if pre==arr:
                count+=1
          
        return count
    
      