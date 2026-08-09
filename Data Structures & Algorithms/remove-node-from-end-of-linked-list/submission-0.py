# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0

        dummy = ListNode(0, head) #dummy points to real head of list
        left = dummy
        curr = head

        while i < n:
            curr = curr.next #traverse until u get to the node u wanna remove
            i += 1

        while curr:
            left = left.next
            curr = curr.next

        left.next = left.next.next
        return dummy.next
        
        
