class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        for n in nums:
            if (n - 1) not in nums_set:
                a = 0 
                while (n+a) in nums_set:
                    a += 1
                count = max(a,count)
        return count
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """nums.sort()
        count = 0
        ans  = []
        if not nums:
            return 0
        print(nums)
        for i in range(0, len(nums)-1):
            j= i+1
            if nums[i] + 1 == nums[j]:
                count+=1
                ans.append(nums[i])
            continue
        print(ans)
        return count"""
        