class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        step=(abs(0-target[0])+abs(0-target[1]))
        for i in range(len(ghosts)):
            N=(abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1]))
            if N<=step:
                return False
          
        return True
        
        