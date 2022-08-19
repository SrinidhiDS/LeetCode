class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0) # 2,3
            permutation = self.permute(nums)
            
            for j in permutation:
                j.append(n) # [2,3,1] [3,2,1]
                ans.append(j)
            nums.append(n) #2,3,1
        return ans
        