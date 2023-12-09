class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        count={}
        for win,loser in matches:
            count[win]=count.get(win,0)
            count[loser]=count.get(loser,0)+1
        no_match=[]
        one_match=[]
        for player,loss in count.items():
            if loss==0:
                no_match.append(player)
            if loss==1:
                one_match.append(player)
        return(sorted(no_match),sorted(one_match))