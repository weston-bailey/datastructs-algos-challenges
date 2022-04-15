const assert = require("chai").assert
const { 
  Node, 
  BinarySearchTree 
} = require("./BinarySearchTree")

describe("Node", () => {
  const value = 10
  const node = new Node(value)
  it("should have a left prop", () => {
    assert.property(node, "left")
  })

  it("should have a right prop", () => {
    assert.property(node, "right")
  })

  it("should have a value", () => {
    assert.property(node, "value")
  })
  
  it("value should be 10", () => {
    assert.equal(node.value, 10)
  })
})

describe("BinarySearchTree", () => {
    const bst = new BinarySearchTree(10)
    bst.insert(8).insert(12).insert(7).insert(9).insert(11).insert(15)
    it("should have a head prop", () => {
      assert.property(bst, "head")
    })

    it("head's value should be 10", () => {
      assert.equal(bst.head.value, 10)
    })

    it("head has a left with a value of 8", () => {
      assert.equal(bst.head.left.value, 8)
    })

    it("head has a right with a value of 12", () => {
      assert.equal(bst.head.right.value, 12)
    })

    it("left has a left with a value of 7", () => {
      assert.equal(bst.head.left.left.value, 7)
    })

    it("left has a right with a value of 9", () => {
      assert.equal(bst.head.left.right.value, 9)
    })

    it("right has a left with a value of 11", () => {
      assert.equal(bst.head.right.left.value, 11)
    })

    it("right has a right with a value of 15", () => {
      assert.equal(bst.head.left.right.value, 15)
    })

})