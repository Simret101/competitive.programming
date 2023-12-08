class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        store = {}
        
        for path in paths:
            arr = path.split(" ")
            directory = arr[0]
            
            for i in range(1, len(arr)):
                file_info = arr[i]
                file_start = file_info.index("(")
                fileName = file_info[:file_start]
                content = file_info[file_start + 1: -1]
                if content not in store:
                    store[content] = []
                store[content].append(directory + "/" + fileName)
        
        store = {k: v for k, v in store.items() if len(v) >= 2}
        
        return list(store.values())
        