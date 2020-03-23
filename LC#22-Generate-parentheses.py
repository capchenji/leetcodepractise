class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        collection = [('(', 1, 0)]
        occ = []
        for i in range(2*n-1):
            for j in collection:
                if j[1]<n:
                    occ.append((j[0]+'(', j[1]+1, j[2]))
                if j[2]<j[1]:
                    occ.append((j[0]+')', j[1], j[2]+1))
            collection = occ
            occ = []
        
        return [item[0] for item in collection]
            
