class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapst, mapts = {} , {}
        
        for char1,char2 in zip(s , t):
            
            if ((char1 in mapst) and (mapst[char1] != char2) or (char2 in mapts) and (mapts[char2] != char1)):
                return False
            
            mapst[char1] = char2
            mapts[char2] = char1
        return True