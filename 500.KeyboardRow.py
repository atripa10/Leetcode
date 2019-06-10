class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        topRow = set('qwertyuiop')
        middleRow = set('asdfghjkl')
        bottomRow = set('zxcvbnm')
        ans =[]
        for word in words:
            temp = set(word.lower())
            if topRow & temp == temp:
                ans.append(word)
            if middleRow & temp  == temp:
                ans.append(word)
            if bottomRow & temp == temp:
                ans.append(word)
        return ans
