class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ans = ''
        li = []  
        for c in str:
            if ord(c) >= 65 and ord(c) <= 90:
                li.append(chr(ord(c) + 32))
            else:
                li.append(c)
        return ans.join(li)
