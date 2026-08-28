# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        res = head
        while res:
            arr.append(res)
            res = res.next
        i, j = 1, len(arr) - 1
        if not arr:
            return None
        while i <= j:
            head.next = arr[j]
            head = head.next
            head.next = arr[i]
            head = head.next
            i += 1
            j -= 1
        head.next = None


        
        