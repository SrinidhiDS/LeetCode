class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            hash_ans[tuple(count)].append(s)
            
        return hash_ans.values()
        
        