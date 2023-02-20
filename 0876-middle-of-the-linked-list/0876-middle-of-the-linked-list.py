# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head  # Initialize the slow and fast pointers to the head of the linked list
        while fast and fast.next:  # Traverse the linked list
            slow = slow.next  # Move the slow pointer one step
            fast = fast.next.next  # Move the fast pointer two steps
        return slow  # When the fast pointer reaches the end, the slow pointer points to the middle node
