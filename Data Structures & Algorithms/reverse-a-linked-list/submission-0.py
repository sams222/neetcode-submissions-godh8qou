# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        last_node = None

        while cur:
            next_node = cur.next
            cur.next = last_node
            last_node = cur
            cur = next_node

        return last_node
            

        

