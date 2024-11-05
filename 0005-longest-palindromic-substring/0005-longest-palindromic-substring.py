class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        p = ""
        plen = 0

        for  i in range(len(s)):
            ## odd check
            l,r = i,i
            while l >= 0  and r<len(s) and s[l] == s[r] :
                if r-l+1 > plen :
                    p = s[l:r+1]
                    plen = r-l+1
                l = l-1
                r = r+1
            
            # even check
            l,r = i,i+1 
            while l >= 0  and r<len(s) and s[l] == s[r] :
                if r-l+1 > plen :
                    p = s[l:r+1]
                    plen = r-l+1
                l = l-1
                r = r+1

        return p





