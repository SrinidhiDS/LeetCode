class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join(map(str,digits))) + 1
        x = [i for i in str(x)]
        return x
        