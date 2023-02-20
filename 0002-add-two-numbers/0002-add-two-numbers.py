# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a new ListNode to store the sum
        # of the two input LinkedLists
        dummy = ListNode(0)
        # Initialize two pointers to the head of each LinkedList
        p1, p2, current = l1, l2, dummy
        carry = 0
        # Traverse both LinkedLists simultaneously and add
        # each corresponding pair of nodes along with the
        # carry from the previous addition
        while p1 or p2 or carry:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        # Return the head of the resulting LinkedList
        return dummy.next
