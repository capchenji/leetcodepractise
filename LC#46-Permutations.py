class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        return self.dfs(output, nums)
        
        
    
    def dfs(self, exist_list, new_list):
        if len(new_list)==1:
            return [exist_list + [new_list[0]]]
        else:
            output = []
            for i in range(len(new_list)):
                currentlist = exist_list + [new_list[i]]
                #new_list = new_list[0:i] + new_list[i+1:]
                output += self.dfs(currentlist, new_list[0:i] + new_list[i+1:])
        
        return output
