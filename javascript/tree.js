/**
 * Implementation of tree in javascript
 */

 /**
  * Single Node of a tree
  */
class Node {
  constructor(value) {
    this.value = value;
  }

  getValue() {
    return this.value;
  }

  setLeftChild(node) {
    this.left = node;
  }

  setRightChild(node) {
    this.right = node;
  }

  getLeftChild(node) {
    return this.left ? this.left : false;
  }

  getRightChild(node) {
    return this.right ? this.right : false;
  }
}

/**
 * Represents Tree as a collection of nodes
 */
class Tree {
  setRoot(node) {
    this.root = node;
  }

  /**
   * Print the preorder traversal of the tree
   */
  printPreorderTraversal() {
    this.preorderHelper(this.root);
  }

  preorderHelper(node) {
    if (node !== undefined) {
      this.preorderHelper(node.left);
      console.log(node.value);
      this.preorderHelper(node.right);
    }
  }
}

let tree = new Tree();
let node1 = new Node(1);
let node2 = new Node(2);
let node3 = new Node(3);
let node4 = new Node(4);
let node5 = new Node(5);
let node6 = new Node(6);

node1.setLeftChild(node2);
node1.setRightChild(node3);
node2.setLeftChild(node4);
node2.setRightChild(node5);
node3.setLeftChild(node6);
tree.setRoot(node1);

tree.printPreorderTraversal();