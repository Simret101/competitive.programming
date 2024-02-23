class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max=[]
        tot=0
        for i in range(len(grid)):
            row_max.append(max(grid[i]))
        
        col_max=[]
        
        for i in range(len(grid)):
            mat=[]
            for j in range(len(grid[0])):
                mat.append(grid[j][i])
            col_max.append(max(mat))
      
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans=abs(grid[i][j] - min(row_max[i],col_max[j]) )
                tot+=ans
        return tot

        





