function Node(value) {
  this.value = value;
  this.right = null;
  this.left = null;
}

function BST() {
  this.root = null;
}

BST.prototype.insert = function (value) {
  let node = new Node(value);
  if (!this.root) {
    this.root = node;
  } else {
    let current = this.root;
    while (!!current) {
      if (node.value < current.value) {
        if (!current.left) {
          current.left = node;
          break;
        }
        current = current.left;
      } else if (node.value > current.value) {
        if (!current.right) {
          current.right = node;
          break;
        }
        current = current.right;
      } else {
        break;
      }
    }
  }
  return this;
};

let bst = new BST();
bst.insert(25);
bst.insert(40).insert(20).insert(9).insert(32).insert(15).insert(8).insert(27);

BST.prototype.contains = function (value) {
  let current = this.root;
  while (current) {
    if (value === current.value) return true;
    if (value < current.value) current = current.left;
    if (value > current.value) current = current.right;
  }
  return false;
};

console.log(bst.contains(20));

BST.prototype.getMin = function (node) {
  if (!node) node = this.root;
  while (node.left) {
    node = node.left;
  }
  return node.value;
};

BST.prototype.isValidBST = function () {};
