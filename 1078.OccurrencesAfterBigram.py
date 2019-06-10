class Solution(object):
    def findOcurrences(self, text, first, second):
        li = text.split(" ")
        answer = []
        for i in range (0,len(li)-2):
            if li[i] == first and li[i+1] == second:
                answer.append(li[i+2])
        return answer
