class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#         i=j=0
#         if len(nums)==0:
#             return 0;
        
#         output = []
        
#         while (j<len(nums)):
#             if sum(nums[i:j+1]) < target:
#                 j += 1
#             elif sum(nums[i:j+1]) > target:
#                 output.append(j+1-i)
#                 i += 1
#             else:
#                 output.append(j+1-i)
#                 j += 1
        
#         if len(output)==0:
#             return 0;
#         else:
#             return min(output)
        
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)