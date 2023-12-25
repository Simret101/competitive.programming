class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        store=0
        for i in range(len(mat)):
          
            store+=mat[i][i]+mat[i][len(mat)-1-i]
            
 
        if len(mat)%2!=0:
            mid=len(mat)//2
            store-=mat[mid][mid]

        return store


        