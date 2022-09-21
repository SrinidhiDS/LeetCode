class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = Counter(s)
        ans = -1
        for i in range(len(s)):
            if s[i] in count_s and count_s[s[i]] == 1:
                ans = i
                break
        return ans
            
        