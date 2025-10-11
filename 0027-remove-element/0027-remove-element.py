class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # k = 0

        # for i in len(nums):
        #     if nums[i] == val:
        #         nums.remove()

        for i in range(len(nums)):
            try:
                nums.remove(val)

            except:
                continue

        k = len(nums)

        return k