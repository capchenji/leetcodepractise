class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        output = {}
        output_num = -1

        for i in nums:
            output[i] = output.get(i, 0) + 1
            item = output[i]
            if item >len(nums)/2:
                output_num = i
                break

        return output_num
