class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
                
        bucket_sort = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            bucket_sort[n] = 1 + bucket_sort.get(n,0)
        for n,c in bucket_sort.items():
            freq[c].append(n)
        print(bucket_sort)
        print(freq)  
        ans = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        
        """nums.sort()
        count = collections.Counter(nums)
        print(count)
        #ans= []
        ans = list(count.items())
        return ans"""
        