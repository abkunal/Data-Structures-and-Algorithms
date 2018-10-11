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
  setRoot(value) {
    this.root = new Node(value);
  }
}