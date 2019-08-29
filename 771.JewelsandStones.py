class Solution(object):
    def numJewelsInStones(self, J, S):
        dictS = {}
        sum = 0              
        for character in S:
            if character in dictS:
                dictS[character] += 1
            else:
                dictS[character] = 1
        print dictS
        
        for character in J:
            if character in dictS:
                sum += dictS[character]
        return sum
