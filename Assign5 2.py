# binary min heap implementation
class BinHeap:
    # constructor
    def __init__(self):
        self.heap = []

    def parent(self,j):
        return (j-1)//2

    def left(self, j):
        return 2*j + 1

    def right(self,j):
        return 2*j + 2

    def hasLeft(self,j):
        return self.left(j) < self.size()

    def hasRight(self,j):
        return self.right(j)< self.size()

    def swap(self, i, j):
        t = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = t

    def insert(self, k):
        self.heap.append(k)
        self.upheap(self.size()-1)
# finds minimum
    def find_min(self):
        if len(self.heap)!=0:
            smallest = self.heap[0]
        else:
            return -1
        for i in range(0,len(self.heap)):
            if self.heap[i] < smallest:
                smallest = self.heap[i]
        return smallest

    def del_min(self):
        min = self.find_min()
        self.heap.remove(min)
        return min

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.heap)

    def upheap(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self.upheap(parent)

    def downheap(self,i):
        if self.hasLeft(i):
            left = self.left(i)
            smaller = left
            if self.hasRight(i):
                right = self.right(i)
                if self.heap[right] < self.heap[left]:
                    smaller = right
            if self.heap[smaller] < self.heap[i]:
                self.swap(i, smaller)
                self.downheap(smaller)

    def build_heap(self,List):
        self.heap = List
        self.upheap(self.size()-1)
        self.downheap(0)

import random


# build the heap
b = BinHeap()
b.insert(5)
b.insert(11)
b.insert(3)
b.insert(6)
b.insert(7)

# traverse the heap
print(b.del_min())
print(b.del_min())
print(b.del_min())
print(b.del_min())
print(b.del_min())

for i in range(0,10):
    b.insert(random.randint(0,10))
print(b.heap)








