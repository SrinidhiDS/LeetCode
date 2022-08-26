class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

    
        """if t == "":
            return ""
        
        count_t, count_ans = {}, {}
        for i in t:
            count_t[i] = 1 + count_t.get(i,0)
            
        l = 0
        have,need = 0, len(count_t)
        res,res_len = [-1,-1] , float("infinity")
        for r in range(len(s)):
            c = s[r]
            count_ans[c] = 1 + count_ans.get(i,0)
            
            if c in count_t and count_ans[c] == count_t[c]:
                have += 1
                
            while have == need:
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = (r - l + 1)
                    
                count_ans[s[l]] -= 1
                if s[l] in count_t and count_ans[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
                
        l,r = res
        return s[l : r + 1] if res_len != float("infinity") else "" """
                
                
                
        
    
        