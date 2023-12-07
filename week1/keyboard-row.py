class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for word in words:
            lowercase_word = word.lower()
            for i in keyboard:
                if all(char in i for char in lowercase_word):
                    ans.append(word)
                    break
        return ans