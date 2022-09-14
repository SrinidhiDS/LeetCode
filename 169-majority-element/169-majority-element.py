class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        return max(nums_count,key = nums_count.get)
        