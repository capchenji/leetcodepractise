class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        tempdict = dict()
        keys = list(set(words))
        outputdict = tempdict.fromkeys(keys,0)
        
        for item in words:
            outputdict[item] += 1
        
        
        result = sorted(outputdict.keys(), key = lambda x: (-outputdict[x],x))
        return result[0:k]
