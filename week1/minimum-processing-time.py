class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        res=0
        res2=0
        tasks.sort()
        processorTime.sort(reverse=True)
        # j=0
        # for i in range(len(processorTime)):
        #     if j<len(tasks):
        #         for j in range(j,j+4):           
        #             tot=tasks[j]+processorTime[i]
        #             print(tot)
        #             res1=max(res1,tot)
        # return res1
        ans=[]
        i=0
        while i<len(tasks):
            res=max(tasks[i:i+4])
            ans.append(res)
            i=i+4
        j,k=0,0
        max_tot=0
        while j< len(processorTime) and k<len(ans):
            tot=processorTime[j]+ans[k]
            max_tot=max(max_tot,tot)
            j+=1
            k+=1
        return max_tot




        