# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()
        
        if head == None:
            return False
        
        cur = head
        while cur:
            if cur in seen:
                return True
            else:
                seen.add(cur)
            cur = cur.next
            
        return False

            
