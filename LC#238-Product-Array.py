class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        
        # i forwarding
        # j backwarding
        
        i = len(nums) -1
        j = 0
        forward_list = [1]*len(nums)
        backward_list = [1]*len(nums)
        
        while i >= 0 and j < len(nums):
            if i==len(nums) -1 and j==0:
                forward_list[i] = 1
                backward_list[j] = 1
            else:
                forward_list[i] = forward_list[i+1]*nums[i+1]
                backward_list[j] = backward_list[j-1]*nums[j-1]
            i -= 1
            j += 1
        
        for i in range(0, len(nums)):
            output.append(backward_list[i]*forward_list[i])
            
        return output