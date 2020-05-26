class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(subnet, nums, current, index):

            subnet.append(current[:])
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(subnet, nums, current, i+1)
                current.pop()

            return subnet

        subnet = []
        current = []
        index = 0

        return backtrack(subnet, nums, current, index)
            
