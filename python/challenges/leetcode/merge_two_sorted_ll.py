# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # create a list that both lists will be merged into, it will start with smaller value from the lists
        new_list = ListNode()
        if list1.val < list2.val:
            new_list = list1
            list1 = list1.next
        else:
            new_list = list2
            list2 = list2.next

        # track head for return
        head = new_list
        while list1 or list2:
            # if either list runs out, the other list can be added to the end of the new list
            if not list1:
                new_list.next = list2
                return head
            if not list2:
                new_list.next = list1
                return head

            # pick the smaller value and add it to the list, if they are the same, list2's value will be added
            if list1.val < list2.val:
                temp = list1.next
                new_list.next = list1
                new_list = new_list.next
                list1 = temp
            else:
                temp = list2.next
                new_list.next = list2
                new_list = new_list.next
                list2 = temp

        return head
