"""
Wang-Reverse-Integer.py
    This is a simple program that reverses a given integer x within a 32-bit integer range

by: Kyle Wang
July 17, 2023
"""
class Solution(object):
    def reverse(self, x):
        result = 0
        # flags whether or not the given int x is a positive or a negative value, which will be used in the result
        posNeg = 1
        if x < 0:
            posNeg = -1
        # turn x into absolute value for simplicity as we have already checked if x is positive or negative
        x = abs(x)
        while x:
            # x % 10 returns the last digit of x
            digit = x % 10
            result = result * 10 + digit
            # gets rid of the last digit of x as it has already been used
            x /= 10
        # checks the range of the result
        if (abs(result) < 2**31) and (result != 2**31 - 1):
            return result * posNeg
        else:
            # returns 0 if result is not in range
            return 0
        
        
            
        """
        :type x: int
        :rtype: int
        """
