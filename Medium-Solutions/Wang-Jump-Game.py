"""
Wang-Jump-Game.py
    This program takes a list of ints (nums) and starts from the first index to check whether or not it it possible
    to reach the end of the list using the int values in the list.

by: Kyle Wang
July 12, 2023
"""
class Solution(object):
    def canJump(self, nums):
        result = False
        maxDist = nums[0]
        # if the length of nums is less than or equal to 1, then that means we do not have to jump any distance
        if (len(nums) <= 1):
            result = True
        for i in range(1, len(nums)):
            # checking if the maxDist variable is enough to reach the end of the list
            if (maxDist >= (len(nums) - i)):
                result = True
            # decrement distance of maxDist in order to be in-line with for loop iterations
            maxDist -= 1
            # checks if maxDist can be substituted for a greater distance
            if (maxDist >= 0) and (nums[i] > maxDist) and (nums[0] > 0):
                maxDist = nums[i]
        
        return result
        
        """result = False
        if (len(nums) <= 1):
            result = True
        for i in range(len(nums) - 1):
            if (nums[i] == 0):
                break
            if (nums[i] >= (len(nums) - (i+1))):
                result = True
            
        return result"""   
        
        
        """
        :type nums: List[int]
        :rtype: bool
        """
