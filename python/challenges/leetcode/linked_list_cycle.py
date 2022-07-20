# https://leetcode.com/problems/linked-list-cycle-ii/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        table = {}
        # loop over list and store encountered values in a table, keep track of indexes
        i = 0
        current_node = head
        while current_node:
            # print(current_node.val, table)
            # if a value is already in the table, it is the beginning of a cycle, so we should return it
            if current_node not in table:
                table[current_node] = None
            else: 
                return current_node
            
            i += 1
            current_node = current_node.next
            
        
        # if we make it to the end of the list, no cycle is found
        return None
