import colorama
from HuffmanTree import HuffmanTree
import time
from os import name, system
from colorama import Fore
from art import *


# Uses the user's input to calculate the frequency of each character
# Creates the characters dictionary(table), encoded string, and decoded string
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
    tree.calculate_comp_ratio(input_stream)
    coded_string = tree.encoded_string
    tree.decode_coded_string(coded_string)
    return tree


# Prints the options list
def show_list(input_stream):
    system("cls" if name == "nt" else "clear")
    tprint('Huffman', font='sub-zero')
    print(Fore.LIGHTRED_EX + '(i)' + Fore.YELLOW + ' Your string is:')
    time.sleep(0.05)
    print(f'" {input_stream} "\n')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(1)' + Fore.YELLOW + ' Show encoded characters')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(2)' + Fore.YELLOW + ' Show encoded string')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(3)' + Fore.YELLOW + ' Draw the final Huffman tree')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(4)' + Fore.YELLOW + ' Decode the coded string')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(5)' + Fore.YELLOW + ' Enter another string')
    time.sleep(0.05)
    print(Fore.MAGENTA + '(6)' + Fore.YELLOW + ' Exit')
    time.sleep(0.05)


# Clears everything in terminal and prints the title
def show_title():
    system("cls" if name == "nt" else "clear")
    tprint('Huffman', font='sub-zero')


def main():
    colorama.init(autoreset=True)
    show_title()
    input_string = input(Fore.GREEN + 'Enter the string you want to get encoded:\n' + Fore.RESET)
    huff_tree = HuffmanTree()
    process_input_stream(input_string, huff_tree)

    # Checks and process the user choice
    while True:
        show_list(input_string)
        user_input = input(Fore.LIGHTBLUE_EX + '\nChoose an option' + Fore.RED + ' ---> ' + Fore.RESET)

        if user_input == '1':
            show_title()
            for code in huff_tree.huff_codes:
                print(Fore.GREEN + code + Fore.WHITE + ' : ' + Fore.YELLOW + huff_tree.huff_codes[code] + Fore.RESET)
            enter = input('\nPress enter to continue....')
            continue

        elif user_input == '2':
            show_title()
            print('The encoded string:\n')
            print(Fore.GREEN + f'" {huff_tree.encoded_string} "' + Fore.RESET)
            print(Fore.YELLOW + '\nCompression ratio: ' + Fore.GREEN + '{0:.2f}'.format(huff_tree.comp_ratio) + '%' + Fore.RESET)
            enter = input('\nPress enter to continue....')
            continue

        elif user_input == '3':
            huff_tree.draw_tree()
            continue

        elif user_input == '4':
            show_title()
            print('The result of decoding ' + Fore.GREEN + f'" {huff_tree.encoded_string} "' + Fore.RESET + ':\n')
            print(Fore.YELLOW + f'" {huff_tree.decoded_string} "' + Fore.RESET)
            enter = input('\nPress enter to continue....')
            continue

        elif user_input == '5':
            show_title()
            input_string = input(Fore.GREEN + 'Enter your string:\n' + Fore.RESET)
            process_input_stream(input_string, huff_tree)
            continue

        elif user_input == '6':
            break

        else:
            show_title()
            print(Fore.RED + '!!' + 'Choose a valid option' + '!!' + Fore.RESET)
            time.sleep(2.0)


if __name__ == '__main__':
    main()
