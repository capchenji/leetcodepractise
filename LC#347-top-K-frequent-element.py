import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numdict = {}

        for num in nums:
            numdict[num] = numdict.get(num, 0) +1


        heap = []

        for item in numdict:
            heapq.heappush(heap, [numdict[item], item])

            if len(heap)>k:
                heapq.heappop(heap)


        return [item[1] for item in heap]
