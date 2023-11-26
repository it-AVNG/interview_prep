import unittest
from BST import BinarySearchTree

class TestBST(unittest.TestCase):
    '''Test for BST methods'''

    def setUp(self):
        self.input = [2,1,8,5,11]

    def test_BST_inorder(self):
        '''Test inorder search of BST'''
        # In: We visit Left, then visit the Node, then visit the Right branch

        my_tree = BinarySearchTree()
        for item in self.input:
            my_tree.insert(item)

        order = my_tree.inorder_print()

        data = self.input
        data.sort()

        self.assertEqual(data,order)

    # def test_BST_preorder(self):
    #     '''Test preorder search of BST'''
    #     # Pre: We visit Left, then visit Right, then Visit Node
    #     pass

    # def test_BST_postorder(self):
    #     '''Test postorder search of BST'''
    #     # Post: we visit a node, then visit to the left, then visit to the right
    #     pass


if __name__ == '__main__':
    unittest.main()