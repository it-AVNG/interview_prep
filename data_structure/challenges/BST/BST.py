'''
Create a Binary Search Tree structure
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _r_insert(self,current_node,val):
        '''helper function to recursively insert'''

        # if the node is none, place the value
        if current_node == None:
            new_node = Node(val)
            return new_node

        if current_node.val < val:
            current_node.right = self._r_insert(current_node.right, val)
        else:
            current_node.left = self._r_insert(current_node.left, val)

        return current_node

    def insert(self, value):
        '''insert a value to the BST'''

        # if tree is empty, place value at root
        if self.root == None:
            self.root = Node(value)
            return

        # compare the value with the root value
        if self.root.val < value:
            # right branch
            self.root.right = self._r_insert(self.root.right, value)
        else:
            # left branch
            self.root.left = self._r_insert(self.root.left,value)


    def _inorder(self,current_node,order):
        if current_node == None:
            return
        self._inorder(current_node.left,order)
        # print(current_node.val)
        order.append(current_node.val)
        self._inorder(current_node.right,order)

        return order

    def inorder_print(self):
        if self.root == None:
            return
        order = []
        self._inorder(self.root.left, order)
        # print(self.root.val)
        order.append(self.root.val)
        self._inorder(self.root.right,order)

        return order
