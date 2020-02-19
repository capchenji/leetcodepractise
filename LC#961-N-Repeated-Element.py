class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        s = set()
        
        for i in A:
            if i not in s:
                s.add(i)
            else:
                break
        
        return i
