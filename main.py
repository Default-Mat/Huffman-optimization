from HuffmanTree import HuffmanTree
import time
import os


def process_input_stream(input_stream, tree):
    chars = {}
    for char in input_stream:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    tree.build_huffman_tree(chars)
    tree.encode_chars()
    tree.encode_sample_string(input_stream)
    coded_string = tree.encoded_string
    tree.decode_coded_string(coded_string)
    return tree


def main():
    input_string = input('Enter your string:\n')
    huff_tree = HuffmanTree()
    process_input_stream(input_string, huff_tree)

    while True:
        print('\n------------------------------------------------\n')
        print('1.Show encoded character\n2.Show encoded string\n'
              '3.Draw the final Huffman tree\n4.Enter another string\n5.Exit\n\nChoose an option: ')
        user_input = input()

        if user_input == '1':
            for code in huff_tree.huff_codes:
                print(f'{code} : {huff_tree.huff_codes[code]}')
                continue
            time.sleep(2.0)

        if user_input == '2':
            print(huff_tree.encoded_string)
            time.sleep(2.0)
            continue

        if user_input == '3':
            huff_tree.draw_tree()
            time.sleep(2.0)
            continue

        if user_input == '4':
            print('\n------------------------------------------------\n')
            input_string = input('Enter your string:\n')
            process_input_stream(input_string, huff_tree)
            continue

        if user_input == '5':
            break


if __name__ == '__main__':
    main()
