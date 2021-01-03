class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]*len(s)
        
        for i in range(len(s)):
            for jstring in wordDict:
                if s[i-len(jstring)+1:i+1]==jstring and (dp[i-len(jstring)]==True or i-len(jstring)==-1):
                    dp[i] = True;
        
        return dp[-1]