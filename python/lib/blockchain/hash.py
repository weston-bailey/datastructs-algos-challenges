import hashlib

class Node:
    def __init__(self, value, previous_hash='head'):
        self.value = value
        self.previous_hash = previous_hash
        self.next = None
        self.hash = Node.make_hash(self.value, self.previous_hash)

    def __str__(self):
        return f'{self.hash} : {self.value}\n'

    @staticmethod
    def make_hash(value, previous_hash):
        # hash together the previous hash, the value
        history = str(value) + previous_hash
        return hashlib.sha256(history.encode()).hexdigest()

    @staticmethod
    def validate(left_node, right_node):
        if right_node.hash == Node.make_hash(right_node.value, left_node.hash):
            return True
        else:
            return False

def main():
    # The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
    # encode = 'A'.encode()
    # print(encode)
    # # hexdigest turns hash object into a hashed string
    # print(hashlib.sha256(encode).hexdigest())
    # # notice how every print statement returns the same hash with th same input
    # print(hashlib.sha256(encode).hexdigest())
    # print(hashlib.sha256(encode).hexdigest())
    # print(hashlib.sha256(encode).hexdigest())
    head = Node(0)
    one = Node(1, head.hash)
    head.next = one
    two = Node(2, one.hash)
    one.next = two
    three = Node(3, two.hash)
    two.next = three
    print(head, one, two, three)
    print(Node.validate(one, two)) # True
    print(Node.validate(one, three)) # False
    print(Node.validate(two, three)) # True
    two.value = 500
    print(Node.validate(one, two)) # False



if __name__ == '__main__':
    main()
