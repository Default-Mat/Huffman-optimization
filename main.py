from HuffmanTree import HuffmanTree


def main():
    something = "Eerie eyes seen near lake."
    chars = {}
    for char in something:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    huff_tree = HuffmanTree()
    huff_tree.build_huffman_tree(chars)
    huff_codes = huff_tree.encode_chars()
    print(huff_codes)


if __name__ == '__main__':
    main()
