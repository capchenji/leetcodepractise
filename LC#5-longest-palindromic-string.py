class Solution:
    
    def getPalindrome(self, s, l, r):
        stringSum = 0;
        while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
            l -= 1
            r += 1
        
        return s[l+1:r];
    
    def longestPalindrome(self, s: str) -> str:
        
        output = ""
        temp = 0;
        for i in range(len(s)):
            
            tempString = self.getPalindrome(s, i, i)
            if(len(tempString)>temp):
                temp = len(tempString);
                output = tempString;
                
            tempString = self.getPalindrome(s, i, i+1)
            if(len(tempString)>temp):
                temp = len(tempString);
                output = tempString;
        return output;