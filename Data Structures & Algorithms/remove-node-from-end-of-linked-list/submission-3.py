# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        
        while curr:
            curr = curr.next
            length += 1

        prev_node = dummy = ListNode(0, head)
        prev = length - n 

        while prev > 0:
            prev_node = prev_node.next
            prev -= 1

        # prev sits right before the node we intend to remove
        to_remove = prev_node.next
        if to_remove.next is None:
            prev_node.next = None
        
        else:
            prev_node.next = to_remove.next

        return dummy.next
            
        
        
