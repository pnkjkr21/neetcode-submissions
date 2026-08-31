# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            length += 1
        to_remove = length - n

        res = head
        if to_remove == 0:
            return head.next
        while res:
            if to_remove == 1:
                print(to_remove, res.val)
                res.next = res.next.next
            res = res.next
            to_remove -= 1
        return head
            
        