class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        else:
            ans = ""
            i = 0
            for j in range(0,len(t)):
                if i < len(s):
                    if (s != "" and s[i] == t[j]):
                        ans += t[j]
                        i += 1
            if ans == s:
                return True
            else:
                return False
                
        