'''
construct a heap manually
'''

class maxHeap:
    '''implement a maxheap data structure'''

    def __init__(self):
        '''initialize the order of the heap with array'''
        self.map = [None] # use dummy element to add the heap index from 1

    def parent(self, i):
        '''Find the parrent of node i'''
        return i // 2

    def left_child(self, i):
        '''find the left child of node i'''
        return 2 * i

    def right_child(self, i):
        '''find the right chidle of node i'''
        return 2 * i + 1

    def get(self, i):
        '''get the value of node i'''
        return self.map[i]

    def size(self):
        '''return the size of heap'''
        return len(self.map) - 1

    def get_max(self):
        '''return the max of the heap'''
        return self.map[1]

    def extract_max(self):
        '''extract the value from the heap one by one'''

        if self.size() == 0:
            return None  # Heap is empty (only contains the dummy element)

        root_value = self.get_max()

        self.map[1] = self.map[-1]
        del self.map[-1]

        self.heapify(1)

        return root_value

    def insert(self, node):
        '''insert a new node and ensure heap priority'''

        i = self.size() + 1
        self.map.append(node)

        # check if child is larger than parent
        while i !=1 and self.get(self.parent(i)) < self.get(i):
            # If child is larger than parrent, swap place
            self.map[i], self.map[self.parent(i)] = (
                self.map[self.parent(i)],self.map[i]
            )
            # keep the index point to the new added value
            i = self.parent(i)

    def heapify(self, i):
        '''ensure heap priority after extract the node'''

        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        if left <= self.size() and self.get(left) > self.get(i):
            largest = left

        if right <= self.size() and self.get(right) > self.get(largest):
            largest = right

        if largest!=i:
            self.map[i], self.map[largest] = (
                self.map[largest],self.map[i]
            )
            self.heapify(largest)

class minHeap:
    '''implement a minheap data structure'''

    def __init__(self):
        '''initialize the order of the heap with array'''
        self.map = [None] # use dummy element to add the heap index from 1

    def parent(self, i):
        '''Find the parrent of node i'''
        return i // 2

    def left_child(self, i):
        '''find the left child of node i'''
        return 2 * i

    def right_child(self, i):
        '''find the right chidle of node i'''
        return 2 * i + 1

    def get(self, i):
        '''get the value of node i'''
        return self.map[i]

    def size(self):
        '''return the size of heap'''
        return len(self.map) - 1

    def get_min(self):
        '''return the min of the heap'''
        return self.map[1]

    def insert(self, node):
        '''insert a new node and ensure heap priority'''

        i = self.size() + 1
        self.map.append(node)

        # check if child is smaller than parent
        while i !=1 and self.get(self.parent(i)) > self.get(i):
            # If child is smaller than parrent, swap place
            self.map[i], self.map[self.parent(i)] = (
                self.map[self.parent(i)],self.map[i]
            )
            # keep the index point to the new added value
            i = self.parent(i)

    def extract_min(self):
        '''extract the value from the heap one by one'''

        if self.size() == 0:
            return None  # Heap is empty (only contains the dummy element)

        root_value = self.get_min()

        self.map[1] = self.map[-1]
        del self.map[-1]

        self.heapify(1)

        return root_value

    def heapify(self, i):
        '''ensure heap priority after extract the node'''

        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        if left <= self.size() and self.get(left) < self.get(i):
            largest = left

        if right <= self.size() and self.get(right) < self.get(largest):
            largest = right

        if largest!=i:
            self.map[i], self.map[largest] = (
                self.map[largest],self.map[i]
            )
            self.heapify(largest)
