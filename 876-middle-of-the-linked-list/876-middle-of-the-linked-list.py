# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        count = 0
        while dummy.next != None:
            count+=1
            dummy = dummy.next
        mid = count // 2
        if count % 2 == 0:
            for i in range(mid):
                temp = head
                head = head.next
            return head
        else:
            mid =mid+1
            for i in range(mid):
                temp = head
                head = head.next
            return head
        