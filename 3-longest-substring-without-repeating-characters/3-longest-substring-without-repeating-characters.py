class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = {}
        ans = 0
        l = 0
        for r in range(0, len(s)):
            if s[r] in charset:
                l = max(l, charset[s[r]] + 1)
            ans = max(ans, r-l + 1)
            charset[s[r]] = r
 
        return ans