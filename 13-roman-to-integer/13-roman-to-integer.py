class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I' : 1, 'V' : 5, 'X': 10, 'L': 50, 'C':100, 'D':500,'M':1000}
        n = len(s)
        num = dic[s[n-1]]
        for i in range(n-2,-1,-1):
            if dic[s[i]] >= dic[s[i+1]]:
                num += dic[s[i]]
            else:
                num -= dic[s[i]]
        return num
        