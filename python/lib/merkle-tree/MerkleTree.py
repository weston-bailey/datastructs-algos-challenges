import hashlib

class Node:
    def __init__(self, value,  left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    @staticmethod
    def hash(val):
        return hashlib.sha256(val.encode('utf-8')).hexdigest()

    @staticmethod
    def double_hash(val):
        return Node.hash(Node.hash(val))

class MerkleTree:
    pass

def main():
    root = Node('root', Node('left'), Node('right'))
    print(root.value, root.left.value, root.right.value)
    root.left.value = Node.hash(root.left.value)
    root.right.value = Node.hash(root.right.value)
    root.value = Node.hash(root.left.value + root.right.value)
    print(root.value, root.left.value, root.right.value)

if __name__ == '__main__':
    main()
