from MaxHeapTree import MaxHeap
from Node import Node


class HuffmanTree:
    def __init__(self):
        self.root = Node()
        self.huff_codes = {}
        self.encoded_string = ''
        self.decoded_string = ''

    def build_huffman_tree(self, char_list):
        priority_list = MaxHeap()
        for char in char_list:
            root = Node(char_list[char], char)
            priority_list.insert(root)

        while priority_list.get_length() > 1:
            first = priority_list.delete()
            second = priority_list.delete()
            sum_of_freqs = first.freq + second.freq
            root = Node(sum_of_freqs)
            root.left = first
            root.right = second
            priority_list.insert(root)

        self.root = priority_list.delete()

    def encode_chars(self):
        string = ''
        self.__code_chars(self.root, string)
        return self.huff_codes

    def __code_chars(self, root, string):
        if root.left is None and root.right is None:
            self.huff_codes[string] = root.char
            return True

        elif root is None:
            return False

        string += '0'
        is_char = self.__code_chars(root.left, string)
        if is_char:
            string = string[:-1]
        string += '1'
        self.__code_chars(root.right, string)
        return True

    def encode_sample_string(self, string):
        for char in string:
            for huff_code in self.huff_codes:
                if char == self.huff_codes[huff_code]:
                    self.encoded_string += huff_code

    def decode_coded_string(self, coded_string):
        string = ''
        char_code = ''
        for char in coded_string:
            char_code += char
            if char_code in self.huff_codes:
                string += self.huff_codes[char_code]
                char_code = ''
        self.decoded_string = string
