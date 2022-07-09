import hashlib

class Node:
    def __init__(self, left, right, value):
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
    pass

if __name__ == '__main__':
    main()
