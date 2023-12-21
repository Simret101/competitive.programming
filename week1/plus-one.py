class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        store = ""
        for i in range(len(digits)):
            store += str(digits[i])

        ans = str(int(store) + 1)
        res = []
        for i in range(len(ans)):
            res.append(int(ans[i]))

        return res