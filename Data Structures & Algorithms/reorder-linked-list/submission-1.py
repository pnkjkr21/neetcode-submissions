# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        res = head
        while res:
            res = res.next
            length += 1
        mid = head
        i = 0
        while i < length // 2 - 1:
            mid = mid.next
            i += 1
        last = self.reverse(mid.next, None)
        mid.next = None
        res = head
        res = res.next
        i = 0
        while res and last:
            if i % 2 == 0:
                head.next = last
                last = last.next
            else:
                head.next = res
                res = res.next
            i += 1
            head = head.next
        if res:
            head.next = res
        if last:
            head.next = last
    
    def reverse(self, head, prev):
        if not head:
            return prev
        nex = head.next
        head.next = prev
        return self.reverse(nex, head)


        
        