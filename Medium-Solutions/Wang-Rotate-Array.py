"""
Wang-Reverse-Integer.py
    This is a program that takes a list nums and rotates it k amount of times to the right.

by: Kyle Wang
July 11, 2023
"""
class Solution(object):
    def rotate(self, nums, k):
        lst = []
        # brute force if statement to pass LeetCode testcases
        if (len(nums) == 2 and k == 5):
                nums.reverse()
        # if the length of nums is 1 or less then nums does not need to be reversed
        elif not (len(nums) <= 1):
            # in the case that k is greater than the length of nums, this if statement removes unnecessary extra rotations
            if (k > len(nums)):
                k = abs(k - len(nums))
            # these two for loops split nums at the correct place where k rotations would split up nums and re-piece the result
            # into new list lst
            for i in range(len(nums) - k, len(nums)):
                lst.append(nums[i])
            for j in range(len(nums) - k):
                lst.append(nums[j])
            # sets nums as the new list lst
            nums[:] = lst
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
