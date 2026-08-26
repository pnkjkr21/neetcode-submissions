# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    
    def reverse(self, node, prev):
        if not node:
            return prev
        nex = node.next
        node.next = prev
        return self.reverse(nex, node)
        