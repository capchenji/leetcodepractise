class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def strsearch(i,j,board,word,stack):
            stack.append((i,j))

            if not word:
                return True

            if i-1>=0 and board[i-1][j]==word[0] and (i-1,j) not in stack:
                if strsearch(i-1,j,board, word[1:],stack):
                    return True
                else:
                    stack.pop()

            if i+1<len(board) and board[i+1][j]==word[0] and (i+1,j) not in stack:
                if strsearch(i+1,j,board, word[1:],stack):
                    return True
                else:
                    stack.pop()

            if j-1>=0 and board[i][j-1]==word[0] and (i,j-1) not in stack:
                if strsearch(i,j-1,board, word[1:],stack):
                    return True
                else:
                    stack.pop()

            if j+1<len(board[0]) and board[i][j+1]==word[0] and (i,j+1) not in stack:
                if strsearch(i,j+1,board, word[1:],stack):
                    return True
                else:
                    stack.pop()


        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0]==board[i][j]:
                    stack = []
                    if strsearch(i,j,board,word[1:],stack):
                        return True

        return False
