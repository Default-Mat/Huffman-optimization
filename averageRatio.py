from HuffmanTree import HuffmanTree


def show_average_ratio():
    with open('100Strings.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    sample_strings = []
    for line in lines:
        sample_strings.append(line.strip())

    chars = {}
    sum_of_ratios = 0
    for string in sample_strings:
        for char in string:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        tree = HuffmanTree()
        tree.build_huffman_tree(chars)
        tree.encode_chars()
        tree.encode_sample_string(string)
        tree.calculate_comp_ratio(string)
        sum_of_ratios += tree.comp_ratio
        tree.root = None
        del tree

    print(sum_of_ratios / 100)


if __name__ == '__main__':
    show_average_ratio()
