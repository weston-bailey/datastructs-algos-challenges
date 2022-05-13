from dataclasses import dataclass


@dataclass
class Node:
    '''
        a node for the linked list
    '''
    value: any
    next: any = None

    def __repr__(self):
        return f'{(self.value)}'


test_node = Node(5)
test_node.next = Node(10)


class List:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node
            current_node = current_node.next

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return self

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

        return self


ll = List()

for i in range(20):
    ll.add(i)


for i in ll:
    print(i)

print(ll.head, ll.head.next)
