# matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]

# N = len(matrix[0])  #N=5
# print(N)
# i = 0
# while N-2*i-1>=0:
#   j = i
#   print(j)
  
#   print('i==='+str(i))
#   print('hhahaha' , str(N-2*i-1))
#   M = N - 2*i
#   M = N - 1 - i
#   print('MMMMM' , str(M))
#   while j < M:
#     print('getint')
#     print("loop---clear"+str(i))
#     print('loop'+str(j))
#     temp = matrix[j][M -1]
#     print(temp)
#     matrix[j][M -1] = matrix[i][j]
#     print(matrix)
#     temptwo = matrix[M -1][M -1-j]
#     print(temptwo)
#     matrix[M -1][M - j -1] = temp
#     print(matrix)
#     print('-----')
#     temp = matrix[M - j -1][i]
#     print(temp)
#     matrix[M - j -1][i] = temptwo
#     print(matrix)
#     matrix[i][j] = temp
#     print(matrix)
#     j += 1

#   # N = N-2
#   i += 1

# print(matrix)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0]) 
        i = 0
        while N-2*i-1>=0:
          j = i
          M = N - 1 - i
          while j < M:
            q = N - 1 - j
            temp = matrix[i][j]
            matrix[i][j] = matrix[q][i]
            matrix[q][i] = matrix[M][q]
            matrix[M][q] = matrix[j][M]
            matrix[j][M] = temp
            j += 1

          i += 1

        return matrix
    
# (0,0) -> (0,4) ->(4,4) ->(4,0) ->(0,0)

# (0,1) -> (1,4) ->(4,3)->(3,0) ->(0,1)

# (0,2) -> (2,4) ->(4,2)->(2,0) -> (0,2)

# (0,3) -> (3,4) ->(4,1)->(1,0) -> (0,3)

# (1,1) -> (1,3) -> (3,3) ->(3,1) ->(1,1)

# (i,j) -> (j, N) -> (N, N-j) -> (N-j,i)->(i,j)

# (1,2) -> (2,3) -> (3,2) ->(2,1) ->(1,2)

# N - 2*j -1
        
            
            