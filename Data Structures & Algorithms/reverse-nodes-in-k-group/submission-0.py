# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k <= 1:
            return head


        dummy =  ListNode(0, head)
        prev_group_end = dummy # we act as though dummy is the end 
                               # to a non-existent, prev group
                               # this helps to maintain same logic throughout

        while True:
            fast = prev_group_end # fast will end up at the last item
                                  # in the current group
            for i in range(k):
                if fast:
                    fast = fast.next
                else:
                    break
            
            if not fast:
                break

            prev = fast.next           
            curr = prev_group_end.next 
            sub_head = curr            

            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            prev_group_end.next = fast
            prev_group_end = sub_head



        return dummy.next
            




            

        
                