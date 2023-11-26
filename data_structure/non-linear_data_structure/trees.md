# Non-linear Data structure: Tree
A tree has nodes. Tree Node can store any value of anytype.
On top of the storing data. We also stored node connections.
These connections point to other Nodes. In a Tree, we can only access to Root Node.
From the Root Node, we can traverse to other nodes as needed.

## Properties
+ Node: a Tree node
+ Edge: A relationship between a parent-child relationship
+ Root: the very first node that the entry point.
+ Leaf: a node that has no children.
+ Depth: the layer that we traverse from the the root node, with every level we go down from the root node, the depth increase by 1
+ Height: how deep is the tree

## Binary tree:
Every single parent Node has exactly 2 children

### Binary search Tree:
A binary tree is where the value are sorted. Everything on left is less than the node value.
Also everythin on the right is larger than the node value. A binary search tree does not allow duplicate.

#### AVL tree:
When a Binary Search Tree is balance. Which means all the node of the left and the right has the same number of node


## Red Black Tree:
A tree that has color defined node.

## B Tree:
Multilevel, balanced, sorted tree, that each nodes has more than 2 children.

## Operation on a Tree:
+ Search: for normal tree, it is O(n) but for BST, it is O(logn)
+ Sort: it is O(logn), traverse the given tree
+ Delete: If the position is known, it is O(1). If not, depending on the tree it is either O(logn) or O(n)
+ Insert: the same as Deletion.

### Traversal

There are 3 typically 3 ways to traverese: In order, Pre order, Post order.
+ Post: we visit a node, then visit to the left, then visit to the right
+ In: We visit Left, then visit the Node, then visit the Right branch
+ Pre: We visit Left, then visit Right, then Visit Node

TODO: construct a Tree that has all the operation and properties

## Uses of Tree:
### Database management system.
BST, AVL,RB,B-tree is very powerfull in seperating element. Indexing and labeling is fast as well
File management is a tree.
Syntax Tree: build a complier for example.
Priority Queue: of course we can use heap, but this can be done.

**insight**: when we create model, it is a tree.

---
==Validate a BST==
Simple: in-order traversal, we will have a sorted value return.

---
TODO: implement a validation method for a BST