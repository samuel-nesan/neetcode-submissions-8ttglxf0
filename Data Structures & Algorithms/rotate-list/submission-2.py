# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        n, cur = 1, head
        
        while cur.next:
            n += 1
            cur = cur.next
        
        k = k % n
        cur.next = head

        for i in range(n - k):
            cur = cur.next
        
        head = cur.next
        cur.next = None
        return head
                


        
            
            
            