from HuffmanTree import HuffmanTree


def main():
    something = "در این راستا"
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
    huff_tree.encode_sample_string(something)
    coded_string = huff_tree.encoded_string
    print(coded_string)
    huff_tree.decode_coded_string(coded_string)
    print(huff_tree.decoded_string)


if __name__ == '__main__':
    main()
