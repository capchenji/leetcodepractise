class Solution:
    def countBits(self, num: int) -> List[int]:
        
        df = [0]*(num+1)
        
        df[0] = 0
        if len(df)==1:
            return df
        df[1] = 1
        
        for i in range(2,num+1):
            if i%2==0:
                df[i] = df[i//2]
            else:
                df[i] = df[i-1] + 1
        
        return df
