# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        cur, n = head, 1
        while cur.next:
            n += 1
            cur = cur.next
        
        cur.next = head
        k = k % n

        for i in range(n-k):
            cur = cur.next

        newHead = cur.next
        cur.next = None

        return newHead

                


        
            
            
            