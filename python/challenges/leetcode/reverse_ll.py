'''
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []



Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000



Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # create a new list
        temp = head.next
        new_list = head
        new_list.next = None

        current_node = temp
        while current_node:
            # loop over old list, inserting nodes before the head of the new list
            temp = current_node.next
            current_node.next = new_list
            new_list = current_node
            current_node = temp

        # return the last inserted node, it is the head of the new list
        return new_list
