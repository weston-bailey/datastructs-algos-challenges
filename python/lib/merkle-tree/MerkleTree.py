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
    def __init__(self, values):
        self.__build_tree(values)
        self.root = None

    def __build_tree(self, values):
        leaves = [Node(Node.double_hash(value)) for value in values]
        # duplicate last elem if there is an odd number of values
        if len(leaves) % 2 == 1:
           # leaves.append(leaves[len(leaves)- 1])
           leaves.append(leaves[-1:][0])
        self.root = self.__build_tree_rec(leaves)

        # for leaf in leaves:
        #     print(leaf.value)

    def __build_tree_rec(self, nodes):
        pass

    def print_tree(self):
        pass

    def __print_tree_rec(self):
        pass

    def get_root_hash(self):
        pass
def main():
    # testing the node
    # root = Node('root', Node('left'), Node('right'))
    # print(root.value, root.left.value, root.right.value)
    # root.left.value = Node.hash(root.left.value)
    # root.right.value = Node.hash(root.right.value)
    # root.value = Node.hash(root.left.value + root.right.value)
    # print(root.value, root.left.value, root.right.value)
    nodes = ['root', 'left', 'right']
    tree = MerkleTree(nodes)

if __name__ == '__main__':
    main()
