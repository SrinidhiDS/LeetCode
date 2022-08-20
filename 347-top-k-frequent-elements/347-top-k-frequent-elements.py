class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
                
        """bucket_sort = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            bucket_sort[n] = 1 + nums.count(n)
        for n,c in bucket_sort.items():
            freq[c].append(n)
        print(bucket_sort)
        print(freq)  
        ans = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans"""
        
        
        """nums.sort()
        count = collections.Counter(nums)
        print(count)
        #ans= []
        ans = list(count.items())
        return ans"""
        