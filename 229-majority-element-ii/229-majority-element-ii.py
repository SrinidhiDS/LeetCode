class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        ans = set()
        for value in nums_count.values():
            if len(nums)//3 < value:
                for k, v in nums_count.items():
                    if v == value:
                        ans.add(k)
        return ans
                
                
        