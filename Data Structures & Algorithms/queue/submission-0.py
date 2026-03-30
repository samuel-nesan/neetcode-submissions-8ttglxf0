class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left, self.right = ListNode(-1), ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def append(self, value: int) -> None:
        node , prev, next = ListNode(value), self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def appendleft(self, value: int) -> None:
        node, prev, next = ListNode(value), self.left, self.left.next
        prev.next = node
        node.next = next
        node.prev = prev
        next.prev = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else: 
            val, prev, next = self.right.prev.val, self.right.prev.prev, self.right
            prev.next = next
            next.prev = prev
            return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            val, prev, next = self.left.next.val, self.left, self.left.next.next
            prev.next = next
            next.prev = prev
            return val
        
