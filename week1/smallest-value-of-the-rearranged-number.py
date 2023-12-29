class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        num_list = list(num_str)
        num_list.sort()
        
        if num_list[0] == '0':
            for i in range(1, len(num_list)):
                if num_list[i] != '0':
                    num_list[0], num_list[i] = num_list[i], num_list[0]
                    break
        elif num_list[0] == '-':
            num_list.remove('-') 
            num_list.sort(reverse=True)  
            num_list = ['-'] + num_list  
        
        return int(''.join(num_list))