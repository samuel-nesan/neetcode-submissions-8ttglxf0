# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0: return None

        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return dummy.next
        
        def mergeSort(arr, l, r):
            if l > r:
                return None
            if l == r:
                return arr[l]
            
            m = l + (r - l) // 2

            left = mergeSort(arr, l, m)

            right = mergeSort(arr, m + 1, r)
            
            return merge(left, right)

        return mergeSort(lists, 0, len(lists) - 1)


