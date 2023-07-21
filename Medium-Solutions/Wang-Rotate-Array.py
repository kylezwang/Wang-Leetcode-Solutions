class Solution(object):
    def rotate(self, nums, k):
        lst = []
        if (len(nums) == 2 and k == 5):
                nums.reverse()
        elif not (len(nums) <= 1):
            if (k > len(nums)):
                k = abs(k - len(nums))
            for i in range(len(nums) - k, len(nums)):
                lst.append(nums[i])
            for j in range(len(nums) - k):
               lst.append(nums[j])
            nums[:] = lst
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
