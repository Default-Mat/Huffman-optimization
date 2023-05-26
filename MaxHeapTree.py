# We use heapsort for priority list to build our huffman tree
class MaxHeap:
    # Implements a list for heap tree
    def __init__(self):
        self.heap_list = []

    # Inserts the element at the end of the list and sorts it
    def insert(self, data):
        self.heap_list.append(data)
        self.__sort()

    # Pops the first element of the list
    def delete(self):
        first = self.heap_list[0]
        self.heap_list.pop(0)
        # self.__sort()
        return first

    def get_length(self):
        return len(self.heap_list)

    # Gets the index of the node and length of the heap to heapify it
    # Everytime it swaps the parent and its child if the child is greater
    def __max_heapify(self, node_index, list_len):
        left_child = 2 * node_index + 1
        right_child = 2 * node_index + 2
        if left_child < list_len and self.heap_list[node_index].freq < self.heap_list[left_child].freq:
            largest = left_child
        else:
            largest = node_index

        if right_child < list_len and self.heap_list[largest].freq < self.heap_list[right_child].freq:
            largest = right_child

        if largest != node_index:
            temp = self.heap_list[node_index]
            self.heap_list[node_index] = self.heap_list[largest]
            self.heap_list[largest] = temp
            self.__max_heapify(largest, list_len)

    # Uses max heapify for the leaves of the heap tree
    def __build_max_heap(self):
        list_len = len(self.heap_list)
        i = int(list_len / 2 - 1)
        while i >= 0:
            self.__max_heapify(i, list_len)
            i -= 1

    # Builds a max heap and everytime it swaps the root and the last element of
    # the max heap and uses heapify to sort the list in ascending order
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
