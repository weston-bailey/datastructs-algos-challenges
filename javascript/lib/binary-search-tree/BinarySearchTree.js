class Node {
  constructor(val) {
    this.right = null
    this.left = null
    this.value = val
  }
}

class BinarySearchTree {
  constructor(head) {
    this.head = head ? new Node(head) : null
  }

  // add a leaf to the tree
  insert(val) {
    const node = new Node(val)
    // if there is no head, set this node to be the head
    if (!this.head) {
      this.head = node
      return this
    }

    return this
  }
  // print nodes in tree
}

module.exports = {
  Node,
  BinarySearchTree
}

// testing
const myNode = new BinarySearchTree()
myNode.insert(10)

console.log(myNode)
