class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans = []
        defanged =''
        for c in address:
            if c == '.':
                ans.append('[.]')
            else:
                ans.append(c)
        return defanged.join(ans)
        
