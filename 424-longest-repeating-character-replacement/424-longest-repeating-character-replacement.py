class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while ((r-l+1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            ans = max((r-l+1),ans)
        return ans
                
        """while l <= r:
            maxf = 0
            for i in range(l,r+1):
                count[s[i]] = s.count(s[:i])
                maxf = 
                res = len(s[:i]) - maxf
                if res <= k:
                    ans = res
                r += 1
            return ans"""
                