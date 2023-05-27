import math


# We use min heap for priority list to build our huffman tree
class MinHeap:
    # Implements a list for heap tree
    def __init__(self):
        self.heap_list = []

    # Inserts the element at the end of the min heap and swaps it
    def insert(self, data):
        self.heap_list.append(data)
        last_element = self.get_length() - 1
        self.swap(last_element)

    # Pops the root, puts the last element in place of root, and heapifies the tree
    def delete(self):
        first = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.get_length() - 1]
        self.heap_list[self.get_length() - 1] = first
        self.heap_list.pop()
        self.__min_heapify(0, self.get_length())
        return first

    def get_length(self):
        return len(self.heap_list)

    # Everytime it Swaps the node and parent if the node is smaller
    def swap(self, node_index):
        parent = math.ceil(node_index / 2) - 1
        if node_index > 0 and self.heap_list[node_index].freq < self.heap_list[parent].freq:
            temp = self.heap_list[node_index]
            self.heap_list[node_index] = self.heap_list[parent]
            self.heap_list[parent] = temp
            self.swap(parent)

    # Gets the index of the node and length of the heap to heapify it
    # Everytime it swaps the parent and its child if the child is smaller
    def __min_heapify(self, node_index, list_len):
        left_child = 2 * node_index + 1
        right_child = 2 * node_index + 2
        if left_child < list_len and self.heap_list[node_index].freq > self.heap_list[left_child].freq:
            smallest = left_child
        else:
            smallest = node_index

        if right_child < list_len and self.heap_list[smallest].freq > self.heap_list[right_child].freq:
            smallest = right_child

        if smallest != node_index:
            temp = self.heap_list[node_index]
            self.heap_list[node_index] = self.heap_list[smallest]
            self.heap_list[smallest] = temp
            self.__min_heapify(smallest, list_len)
