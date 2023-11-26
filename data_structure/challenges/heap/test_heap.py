import unittest
from heap_priority import minHeap, maxHeap

class TestHeap(unittest.TestCase):
    '''Test constructing a heap'''
    def setUp(self):
        self.input = [1,4,7,8,3,28]

    def test_construct_a_minHeap(self):
        '''Test min Heap construct'''

        my_heap = minHeap()
        for item in self.input:
            my_heap.insert(item)

        order = []
        while my_heap.size() != 0:
            order.append(my_heap.extract_min())
        data =self.input
        data.sort()
        self.assertEqual(data, order)

    def test_construct_a_maxHeap(self):
        '''Test max Heap construct'''

        my_heap = maxHeap()
        for item in self.input:
            my_heap.insert(item)

        order = []
        while my_heap.size() != 0:
            order.append(my_heap.extract_max())

        data =self.input
        data.sort(reverse=True)

        self.assertEqual(data, order)

if __name__ == '__main__':
    unittest.main()

