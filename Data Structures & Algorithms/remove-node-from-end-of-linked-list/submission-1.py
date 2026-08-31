class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = right = dummy

        # Keep n nodes between left and right
        for _ in range(n):
            right = right.next

        # Move both until right reaches the end
        while right.next:
            left = left.next
            right = right.next

        # Remove nth node from the end
        left.next = left.next.next

        return dummy.next