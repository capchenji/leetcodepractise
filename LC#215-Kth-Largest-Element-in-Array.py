class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Time Limit Exceeded
#         for i in range(len(nums)):
#             for j in range(i):
                
#                 if nums[i]<nums[j]:
#                     temp = nums[i]
#                     nums[i] = nums[j]
#                     nums[j] = temp
        
#         return nums[len(nums) - k]
    
        # min heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)