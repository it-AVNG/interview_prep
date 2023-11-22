import unittest
from construct import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_Construct_linked_list(self):
        """test create a linked list"""

        my_list = LinkedList()
        self.assertEqual(type(my_list).__name__, "LinkedList")

    def test_insert_linked_list(self):
        """test insert a node into linked list"""

        my_list = LinkedList()
        my_list.insert(5)
        my_list.insert(3)
        self.assertEqual(my_list.head.data, 5)
        self.assertEqual(my_list.head.next.data, 3)

    def test_print_link_list(self):
        my_list = LinkedList()
        my_list.insert(5)
        my_list.insert(3)
        my_list.insert(6)
        check_list = [5, 3, 6]
        self.assertEqual(my_list.print_list(), check_list)


if __name__ == "__main__":
    unittest.main()

