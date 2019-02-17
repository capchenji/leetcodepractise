class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':

        i = 0
        j = 1
        maxlen = 0
        while i<len(s):
            tmplen = 0
            while j<len(s):
                if s[j] not in s[i:j]:
                    tmplen += 1
                    j += 1
                else:
                    break
            if j-i>maxlen:
                maxlen = j-i
            i += 1
            j = i+1

        return maxlen
