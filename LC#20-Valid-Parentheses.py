class Solution:
    def isValid(self, s: 'str') -> 'bool':

        i = 0
        result = []
        testdict = {}
        testdict['['] = ']'
        testdict['('] = ')'
        testdict['{'] = '}'


        while i< len(s):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                result.append(s[i])
            else:
                if len(result)==0:
                    return False
                if testdict[result[-1]] !=s[i]:
                    break
                else:
                    result.pop(-1)
            i += 1

        return len(result)==0
