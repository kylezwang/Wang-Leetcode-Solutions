class Solution(object):
    def removeDuplicates(self, nums):
        lst = []
        for i in range(len(nums)):
            if (lst.count(nums[i]) == 0):
                lst.append(nums[i])
        nums[:] = lst
        k = len(lst)
        return k
              
                
        """
        :type nums: List[int]
        :rtype: int
        """
