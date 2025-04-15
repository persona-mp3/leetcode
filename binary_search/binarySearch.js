
//           a
//          / \
//          b  c 
//         / \  \
//         d  e  f
//
// depthFirstSearch Algo
const depthFirst = function (root) {
  if (root === null) {
    console.log([])
    return 'root is null'
  }
  const callStackExecutionOrder = []
  const stack = [ root ]
  while (stack.length > 0) {
    const curr = stack.pop()
    console.log(curr.value);
    callStackExecutionOrder.push(curr.value)

    if (curr.right) stack.push(curr.right)
    if (curr.left) stack.push(curr.left) 
    
  }
  console.log(callStackExecutionOrder)
}


function depthFirstSearch(root) {
  if (root === null) {
    return []
  }


  const rightValue = depthFirstSearch(root.right)
  const leftValue = depthFirstSeatch(root.left)
}

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const a = new Node('a')
const b = new Node('b')
const c = new Node('c')
const d = new Node('d')
const e = new Node('e')
const f = new Node('f')
const g = null

a.left = b;
a.right = c;

b.left = d;
b.right = e;

c.right = f;


 depthFirstSearch(g)
