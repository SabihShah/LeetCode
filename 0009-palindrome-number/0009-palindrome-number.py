class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x = str(x)

        start = x[:]
        end = x[::-1]

        result = []

        for i in range(len(x)):
            if start[i] == end[i]:
                result.append(True)
            else:
                result.append(False)

        if all(result) == True:
            return True
        else:
            return False
