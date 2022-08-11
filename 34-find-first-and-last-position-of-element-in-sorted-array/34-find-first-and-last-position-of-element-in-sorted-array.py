class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f = self.binarysearch(nums,target,True)
        l = self.binarysearch(nums,target,False)
        return [f,l]
        
    def binarysearch(self, nums, target,left):
        l = 0
        r = len(nums) - 1
        res = -1
        mid = 0
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                res = mid
                if left:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res
                    
        
                
        