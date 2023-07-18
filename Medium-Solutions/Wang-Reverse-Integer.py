class Solution(object):
    def reverse(self, x):
        result = 0
        posNeg = 1
        if x < 0:
            posNeg = -1
        x = abs(x)
        while x:
            digit = x % 10
            result = result * 10 + digit
            x /= 10
        if (abs(result) < 2**31) and (result != 2**31 - 1):
            return result * posNeg
        else:
            return 0
        
        
            
        """
        :type x: int
        :rtype: int
        """
