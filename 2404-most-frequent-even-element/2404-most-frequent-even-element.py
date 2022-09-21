class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums_count = {}
        ans = []
        for i in nums:
            if i%2 == 0:
                nums_count[i] = nums_count.get(i,0) + 1
        if nums_count:
            max_value = max(nums_count.items(),key = lambda x:x[1])
            for k,v in nums_count.items():
                if v == max_value[1]:
                    ans.append(k)     
                    
            if len(ans) > 1:
                return min(ans)
            else:
                return ans[0]
        else:
            return -1
    