class MaxHeap:
    def __init__(self):
        self.heap_list = []

    def insert(self, data):
        self.heap_list.append(data)
        self.__sort()

    def delete(self):
        first = self.heap_list[0]
        self.heap_list.pop(0)
        # self.__sort()
        return first

    def get_length(self):
        return len(self.heap_list)

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

    def __build_max_heap(self):
        list_len = len(self.heap_list)
        i = int(list_len / 2 - 1)
        while i >= 0:
            self.__max_heapify(i, list_len)
            i -= 1

    def __sort(self):
        self.__build_max_heap()
        list_len = len(self.heap_list)
        # temp = []
        last_element = list_len - 1
        while last_element >= 1:
            temp = self.heap_list[0]
            self.heap_list[0] = self.heap_list[last_element]
            self.heap_list[last_element] = temp
            self.__max_heapify(0, last_element)
            last_element -= 1
        # while list_len >= 1:
        #     temp.append(self.heap_list.pop(0))
        #     list_len -= 1
        #
        # self.heap_list = temp

