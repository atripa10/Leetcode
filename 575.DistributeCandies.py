class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        #Solution 1
        '''
        dict = collections.Counter(candies)
        maxUniq = len(candies)/2
        answer = 0
        return min(maxUniq,len(dict))
        '''
        # Solution 2
        '''
        dict = {}
        answer = 0
        for candy in candies:
            if candy not in dict:
                answer+=1
                dict[candy] =1
        return min(answer,len(candies)/2)
        '''
        '''
        #Solution 3
        dict = {}
        answer = 0
        maxUniq = len(candies)/2 # max uniq candies can only be half
        for candy in candies:
            if candy not in dict:
                answer+=1
                if answer == maxUniq:
                    return answer # return answer as soon as maxUniq is reached
                dict[candy] =1
        return min(answer,maxUniq)
        '''

        # Solution 4 with set
        return min(len(set(candies)),len(candies)/2)
