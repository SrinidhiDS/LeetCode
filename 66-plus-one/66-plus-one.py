class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ""
        y = []
        for i in digits:
            x = x + str(i)
        x = int(x) + 1
        x = [i for i in str(x)]
        return x
        