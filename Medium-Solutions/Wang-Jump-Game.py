class Solution(object):
    def canJump(self, nums):
        result = False
        maxDist = nums[0]
        if (len(nums) <= 1):
            result = True
        for i in range(1, len(nums)):
            if (maxDist >= (len(nums) - i)):
                result = True
            maxDist -= 1
            if (maxDist >= 0) and (nums[i] > maxDist) and (nums[0] > 0):
                maxDist = nums[i]
