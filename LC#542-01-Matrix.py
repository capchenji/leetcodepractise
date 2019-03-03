# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#
#         def searchfun(row, col, path):
#             if matrix[row][col] == 0:
#                 return path
#             else:
#                 if (row - 1 >= 0):
#                     pathup = searchfun(row - 1, col, path + 1)
#                 if (col - 1 >= 0):
#                     pathleft = searchfun(row, col - 1, path + 1)
#                 if (col + 1 < colnum):
#                     pathright = searchfun(row, col + 1, path + 1)
#                 if (row + 1 < linenum):
#                     pathbottom = searchfun(row + 1, col, path + 1)
#                 else:
#                     path = 10000
#             return min(pathup, pathleft, pathright, pathbottom)
#
#         eachline = []
#         output = []
#
#         linenum = len(matrix)
#         colnum = len(matrix[0])
#
#         for i in range(0, linenum):
#             tmplist = []
#             for j in range(0, colnum):
#
#                 if matrix[i][j] == 0:
#                     tmplist.append(0)
#                     continue
#                 else:
#                     tmplist.append(searchfun(i, j, 0))
#             output.append(tmplist)
#
#         return output

#using BFS

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        eachline = []
        output = []

        linenum = len(matrix)
        colnum = len(matrix[0])
        queue = []

        for i in range(0, linenum):
            for j in range(0, colnum):

                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = 0x7fffffff

        for i, j in queue:
            for m, n in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                step = matrix[i][j] + 1
                if 0 <= m < linenum and 0 <= n < colnum and matrix[m][n] > step:
                    matrix[m][n] = step
                    queue.append((m, n))

        return matrix
