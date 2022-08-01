class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res =  nums[0]
        total = 0
        for i in nums:
            total += i
            res = max(res,total)
            if total < 0:
                total = 0
        return res
        