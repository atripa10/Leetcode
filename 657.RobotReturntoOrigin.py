class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) % 2 == 1:
            return False
        U, D, L, R = 0, 0, 0, 0
        for m in moves:
            if m == 'U':
                U += 1
            if m == 'D':
                D += 1
            if m == 'L':
                L += 1
            if m == 'R':
                R += 1
        return U == D and L == R
