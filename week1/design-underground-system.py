class UndergroundSystem(object):

    def __init__(self):
      
        self.check_in =defaultdict(tuple)
       
        self.average=defaultdict(list)
   

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in [id]=[stationName,t]
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
    

        distance= t - self.check_in[id][1]
        self.average[(self.check_in [id][0],stationName)].append(distance)

        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

    
        return sum(self.average[(startStation,endStation)])/float(len(self.average[(startStation,endStation)]))



            
        
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)