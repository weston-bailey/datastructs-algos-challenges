class Node {
  constructor(val) {
    this.right = null;
    this.left = null;
    this.value = val;
  }
}

class BinarySearchTree {
  constructor(head) {
    this.head = head ? new Node(head) : null;
  }

  // add a leaf to the tree
  insert(val) {
    const node = new Node(val);
    // if there is no head, set this node to be the head
    if (!this.head) {
      this.head = node;
      return this;
    }

    // start at the head
    let current = this.head;
    while (current) {
      if (node.value > current.value) {
        if (current.right) {
          current = right;
        } else {
          current.right = node;
          current = null;
        }
      } else {
        if (current.left) {
          current = left;
        } else {
          current.left = node;
          current = null;
        }
      }
    }

    return this;
  }
  // print nodes in tree
}

module.exports = {
  Node,
  BinarySearchTree,
};
