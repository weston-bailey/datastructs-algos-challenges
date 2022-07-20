# https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # loop to end of list, to determine the length
        current_node = head
        i = 0
        while current_node:
            i += 1
            current_node = current_node.next
        
        # split len in half, if len is even, add one, if round up
        if i % 2 == 0:
            i = (i // 2) + 1
        else:
            i = math.ceil(i / 2)
        
        j = 0
        current_node = head
        # loop to i - 1, so we don't skip the first node we want
        while current_node and j < i - 1:
            j += 1
            current_node = current_node.next
            
        return current_node
        
