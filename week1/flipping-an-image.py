class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(len(image)):
            res=[]
            for j in range(len(image[0])-1,-1,-1):
                res.append(1-image[i][j])
            ans.append(res)
   
        return ans

        