class Solution:
    def frequencySort(self, s: str) -> str:
        count_s = {}
        ans = ""
        for i in s:
            count_s[i] = count_s.get(i,0) + 1
        
        for i in sorted(count_s,key = lambda x:count_s[x],reverse = True):
            ans += i* count_s[i]
        return ans
            
        