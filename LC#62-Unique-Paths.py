class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        N = n + m - 2
        k = m-1
        
        #C(N,k) = (N-k)! / k!
        up = 1
        down = 1
        for i in range(1, k+1):
            up = up * (N-i+1)
            down = down * i
            
        return int(up/down)