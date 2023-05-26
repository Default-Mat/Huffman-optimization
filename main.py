import colorama

from HuffmanTree import HuffmanTree
import time
from os import name, system
from colorama import Fore
from art import *


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


def show_list():
    system("cls" if name == "nt" else "clear")
    tprint('Huffman', font='sub-zero')
    print(Fore.MAGENTA + '(1)' + Fore.YELLOW + ' Show encoded characters')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(2)' + Fore.YELLOW + ' Show encoded string')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(3)' + Fore.YELLOW + ' Draw the final Huffman tree')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(4)' + Fore.YELLOW + ' Enter another string')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(5)' + Fore.YELLOW + ' Exit')
    time.sleep(0.05)


def main():
    colorama.init(autoreset=True)
    system("cls" if name == "nt" else "clear")
    tprint('Huffman', font='sub-zero')
    print(Fore.YELLOW + '')
    input_string = input(Fore.GREEN + 'Enter the string you want to get encoded:\n' + Fore.RESET)

    huff_tree = HuffmanTree()
    process_input_stream(input_string, huff_tree)

    while True:
        show_list()
        user_input = input(Fore.LIGHTBLUE_EX + '\nChoose an option' + Fore.RED + ' ---> ' + Fore.RESET)

        if user_input == '1':
            system("cls" if name == "nt" else "clear")
            tprint('Huffman', font='sub-zero')

            for code in huff_tree.huff_codes:
                print(f'{code} : {huff_tree.huff_codes[code]}')

            enter = input('\nPress enter to continue....')
            continue

        elif user_input == '2':
            system("cls" if name == "nt" else "clear")
            tprint('Huffman', font='sub-zero')

            print('The encoded string:\n')
            print(huff_tree.encoded_string)
            enter = input('\nPress enter to continue....')
            continue

        elif user_input == '3':
            huff_tree.draw_tree()
            continue

        elif user_input == '4':
            system("cls" if name == "nt" else "clear")
            tprint('Huffman', font='sub-zero')
            input_string = input(Fore.GREEN + 'Enter your string:\n' + Fore.RESET)

            process_input_stream(input_string, huff_tree)
            continue

        elif user_input == '5':
            break

        else:
            system("cls" if name == "nt" else "clear")
            print('Choose a valid option')
            time.sleep(2.0)


if __name__ == '__main__':
    main()
