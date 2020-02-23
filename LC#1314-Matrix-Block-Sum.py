class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        rownum = len(mat)
        colnum = len(mat[0])

        dp = [[0]*(colnum+1) for _ in range(rownum+1)]

        for i in range(rownum):
            #dp[i+1] = 0;
            for j in range(colnum):
                dp[i+1][j+1] = mat[i][j] + dp[i][j+1] + dp[i+1][j] - dp[i][j]


        for i in range(rownum):
            for j in range(colnum):
                r1 = max(0, i-K)
                r2 = min(rownum-1, i+K)
                c1 = max(0, j-K)
                c2 = min(colnum-1, j+K)

                mat[i][j] = dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1] #?

        return mat
    
