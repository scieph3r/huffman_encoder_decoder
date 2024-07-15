import argparse

class Node():
    right = None
    left = None
    def __init__(self, freq = 0, char = None):
        self.char = char
        self.freq = freq

def main():
    # create argument parser
    parser = argparse.ArgumentParser(description="Huffman encoder decoder")

    # add arguments
    parser.add_argument("filepath", type=str, help="the file to be compressed")

    # parse arguments
    args = parser.parse_args()

    fh = None
    date = None

    # open the file
    try:
        fh = open(args.filepath, "r")
    except Exception:
        print(f"unable to open file: {args.filepath}")
        return 1
    
    # read the file
    try:
        data = fh.read()
    except Exception:
        print("Something went wrong:(")
        fh.close()
        return 2
    
    # close the file
    fh.close()
    
    # get character frequency
    char_freq = get_character_count(data)
    
    # map the characters to their frequency and sort them
    char_freq_list = list(map(lambda x: (x, char_freq[x]), char_freq.keys()))
    char_freq_list.sort(key=lambda x: x[1], reverse=True)
    print(char_freq_list)
    
    # create huffman tree
    while len(char_freq_list) > 1:
        left = char_freq_list.pop()
        if not isinstance(left, Node):
            left = Node(freq = left[1], char = left[0])
        right = char_freq_list.pop()
        if not isinstance(right, Node):
            right = Node(freq = right[1], char = right[0])
        new_node = Node(right.freq + left.freq)
        new_node.right = right
        new_node.left = left
        char_freq_list.append(new_node)
        char_freq_list.sort(key=lambda x: x[1] if not isinstance(x, Node) else x.freq, reverse=True)
    
    tree = char_freq_list[0]
    
    return 0

def get_character_count(string):
    chars = {}
    for char in string:
        chars[char] = chars.get(char, 0) + 1
    return chars

if __name__ == "__main__":
    main()
