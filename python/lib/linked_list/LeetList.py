class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} {self.next}'

class LeetList:
    '''
        a linked list that works like leetcode's more or less
    '''
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f'{self.head}'

    # def __iter__(self):
    #     current_node = self.head
    #     if current_node:
    #         yield current_node
    #     current_node = current_node.next

    def add(self, val):
        '''
            add a node to the end of the list
        '''
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return self

        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node
        return self


