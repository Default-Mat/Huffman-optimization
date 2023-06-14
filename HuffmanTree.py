from MinHeapTree import MinHeap
from Node import Node
import tkinter as tk


# This is a modification for canvas.create_oval to make a circle easier
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


class HuffmanTree:
    # We keep the huffman code for every character,
    # encoded string, decoded string, and the root of the huffman tree
    # in the related attributes
    def __init__(self):
        self.root = Node()
        self.huff_codes = {}
        self.encoded_string = ''
        self.decoded_string = ''
        self.comp_ratio = 0

    # Puts the character nodes in the priority list. Then each time it gets the
    # two smallest elements in the list and gives them a parent that has the
    # total frequency. then inserts that parent node in the list
    def build_huffman_tree(self, char_list):
        priority_list = MinHeap()
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

    # clears the dictionary related to character codes and uses __code_chars to
    # code characters
    def encode_chars(self):
        self.huff_codes.clear()
        string = ''
        self.__code_chars(self.root, string)
        return self.huff_codes

    # Iterates the tree. adds 0 to the string everytime it goes left
    # and adds 1 everytime it goes right. If it reaches a leaf, it relates the
    # built code to the character of that leaf in the dictionary
    def __code_chars(self, root, string):
        if root.left is None and root.right is None:
            self.huff_codes[root.char] = string
            return
        self.__code_chars(root.left, string + '0')
        self.__code_chars(root.right, string + '1')

    # Gets the user string and encodes it using characters dictionary(table) called huff_codes
    def encode_sample_string(self, string):
        temp_string = ''
        for char in string:
            temp_string += self.huff_codes[char]
        self.encoded_string = temp_string

    # Gets the coded string and huffman tree root to decode it by iterating the tree
    def decode_coded_string(self, root, coded_string):
        string = ''
        ptr = root
        for i in range(len(coded_string)):
            if coded_string[i] == '0':
                ptr = ptr.left
            else:
                ptr = ptr.right

            if (ptr.right and ptr.left) is None:
                string += ptr.char
                ptr = root

        self.decoded_string = string

    # Sets the canvas window and uses __draw to show the huffman tree
    def draw_tree(self):
        frame = tk.Tk()
        frame.title('Huffman Tree')
        frame.geometry('1000x700+260+50')
        c = tk.Canvas(frame, width=1000, height=700)
        c.pack()
        tk.Canvas.create_circle = _create_circle
        self.__draw(c, 500, 50, 500, 50, 200, 350, 36, 40, self.root)
        frame.mainloop()

    def calculate_comp_ratio(self, string):
        str_len = len(string)
        coded_str_len = len(self.encoded_string)
        size_in_bits = str_len * 8
        ratio = 100 - (coded_str_len / size_in_bits) * 100
        self.comp_ratio = ratio

    # Shows the huffman tree by post-order iterating and drawing the circles, texts, and lines
    # Draws a rectangle instead of circle if it reaches a leaf in the tree and show the character and the frequency
    def __draw(self, canvas, x1, y1, x, y, pixel, rec_pixel, radius, font_size, node):
        if node.left is not None:
            self.__draw(canvas, x, y, x - pixel, y + 100, int(pixel / 2),
                        int(rec_pixel / 2), int(radius / 1.25), int(font_size / 1.25), node.left)

        if node.right is not None:
            self.__draw(canvas, x, y, x + pixel, y + 100, int(pixel / 2),
                        int(rec_pixel / 2), int(radius / 1.25), int(font_size / 1.25), node.right)

        canvas.create_line(x1, y1, x, y, width='3')

        if (node.right and node.left) is None:
            canvas.create_rectangle(x - rec_pixel, y, x + rec_pixel, y + 80, width='2')
            canvas.create_text(x, y + 20, text=node.freq, fill='darkblue', font=f'Helvetica {font_size} bold')
            canvas.create_text(x, y + 60, text=node.char, fill='darkblue', font=f'Helvetica {font_size} bold')
        else:
            canvas.create_circle(x, y, radius, fill='darkblue', width='3')
            canvas.create_text(x, y, text=node.freq, fill='white', font=f'Helvetica {font_size} bold')
