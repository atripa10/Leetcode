class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict = {}
        count = 0
        for w in words:
            temp = ''.join([MORSE[ord(c) - ord('a')]for c in w])
            if temp not in dict:
                dict[temp] = 1
                count += 1
        return count
