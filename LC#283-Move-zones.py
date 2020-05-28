class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = -1

        for i in range(0,len(nums)):
            if nums[i]!=0:
                count +=1
                nums[count] = nums[i]
                if count != i:
                    nums[i] = 0

        if count==-1:
            return [0]
        return nums
