class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        MAX = float('inf')
        dp = [0]+[MAX]*amount
        
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i-c>=0 else MAX for c in coins])+1
        
        if dp[-1]==MAX:
            return -1
        return dp[-1]
    
    
    
    
    
    # def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
    #     dp = [0] + [float('inf') for i in range(amount)]
    #     for i in range(1, amount+1):
    #         for coin in coins:
    #             if i - coin >= 0:
    #                 dp[i] = min(dp[i], dp[i-coin] + 1)
    #     if dp[-1] == float('inf'):
    #         return -1
    #     return dp[-1]