class BinaryTree:
    class Node:
        def __init__(self, data=0):
            self.left = None
            self.right = None
            self.data = data

    def __init__(self, key=None):
        if key is None:
            self.root = None
        else:
            self.root = BinaryTree(key)


class MaxHeap:
    def __init__(self):
        self.heap_list = []

    def insert(self, data):
        self.heap_list.append(data)
        self.__sort()

    def __max_heapify(self, node_index, list_len):
        left_child = 2 * node_index + 1
        right_child = 2 * node_index + 2
        if left_child < list_len and self.heap_list[node_index] < self.heap_list[left_child]:
            largest = left_child
        else:
            largest = node_index

        if right_child < list_len and self.heap_list[largest] < self.heap_list[right_child]:
            largest = right_child

        if largest != node_index:
            temp = self.heap_list[node_index]
            self.heap_list[node_index] = self.heap_list[largest]
            self.heap_list[largest] = temp
            self.__max_heapify(largest, list_len)

    def __build_max_heap(self):
        list_len = len(self.heap_list)
        i = int(list_len / 2 - 1)
        while i >= 0:
            self.__max_heapify(i, list_len)
            i -= 1

    def __sort(self):
        self.__build_max_heap()
        list_len = len(self.heap_list)
        last_element = list_len - 1
        while last_element >= 1:
            temp = self.heap_list[0]
            self.heap_list[0] = self.heap_list[last_element]
            self.heap_list[last_element] = temp
            self.__max_heapify(0, last_element)
            last_element -= 1
