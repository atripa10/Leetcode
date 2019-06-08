class Solution(object):
    def repeatedNTimes(self, A):
        #Solution1 time - O(N), space O(N)
        dict = {}
        '''
        for number in A:
            if number in dict:
                return number
            else:
                dict[number] = 1
         '''
        # Solution 2 time - O(N), space O(1)
        length = len(A)
        for i in range(0, length-1):
            print i
            if i == length-3 :
                if A[i] == A[i+1] or A[i] == A[i+2]:
                    return A[i]
            if i == length-2 :
                if A[i] == A[i+1]:
                    return A[i]
            if i < length - 3:
                if A[i] == A[i+1] or A[i] == A[i+2] or A[i] == A[i+3]:
                    return A[i]
