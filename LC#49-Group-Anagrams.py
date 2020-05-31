class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = {}

        for item in strs:
            a = "".join(sorted(item))

            if a in output:
                output[a] += [item]
            else:
                output[a] = [item]

        return list(output.values())
