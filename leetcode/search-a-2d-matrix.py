class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row=len(matrix)
        c=len(matrix[0])
        def binary(row):
            l=0
            r=c-1
            
            while l<=r:
                mid=(l+r)//2
                if matrix[row][mid]==target:
                    return True
                    
                elif matrix[row][mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
        for i in range(row):
            if binary(i):
                return True
            
        return False

                    
