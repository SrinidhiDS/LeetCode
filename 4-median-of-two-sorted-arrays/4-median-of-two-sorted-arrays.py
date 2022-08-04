class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = list((nums1 + nums2))
        for i in range(0,len(num)):
            for j in range(i+1,len(num)):
                if num[i]>num[j]:
                    num[i],num[j] = num[j],num[i]
        if len(num)%2 == 0:
            mid_id_1 = (len(num)//2 - 1)
            mid_id_2 = (len(num)//2)
            mid_value = (num[mid_id_1] + num[mid_id_2])/2
            return mid_value
        else:
            mid_id = len(num)//2
            return num[mid_id]