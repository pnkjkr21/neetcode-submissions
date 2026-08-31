# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        ans = []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        arr1.reverse()
        arr2.reverse()
        i = len(arr1) - 1
        j = len(arr2) - 1
        rem = 0

        while i >= 0 and j >= 0:
            val = arr1[i] + rem + arr2[j]
            ans.append(val % 10)
            rem = val // 10
            i -= 1
            j -= 1
        while i >= 0:
            ans.append((arr1[i] + rem) % 10)
            rem = (arr1[i] + rem) // 10
            i -= 1
        
        while j >= 0:
            ans.append((arr2[j] + rem) % 10)
            rem = (arr2[j] + rem) // 10
            j -= 1
        
        if rem:
            ans.append(rem)
        
        ans.reverse()
        if len(ans) == 0:
            ans.append(0)
        i = 0
        while ans[i] == 0:
            i += 1
            if i == len(ans):
                i -= 1
                break
        
        ans = ans[i:]
        ans.reverse()
        head = res = ListNode(ans[0])
        for i in range(1, len(ans)):
            head.next = ListNode(ans[i])
            head = head.next
        
        return res

            


        