import argparse

class Node:
    right = None
    left = None
    def __init__(self, freq = 0, char = None):
        self.char = char
        self.freq = freq

class FrequencyTree:
    def __init__(self, root):
        self.root = root

    # TODO: write this pls
    def traverse(self, node, code, mapping):
        if node == None:
            return
        if node.char != None:
            mapping[node.char] = code
            return
        self.traverse(node.right, code + "1", mapping)
        self.traverse(node.left, code + "0", mapping)

    def get_prefix_codes(self):
        mapping = {}
        self.traverse(self.root, "", mapping)
        return mapping
        
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
    
    # garbage collection
    char_freq = None

    # create huffman tree
    tree = create_tree(char_freq_list)
    
    # create prefix code table
    prefix_code_map = tree.get_prefix_codes()
    
    return 0

def create_tree(char_freq_lst):
        lst = char_freq_lst[:]
        while len(lst) > 1:
            left = lst.pop()
            if not isinstance(left, Node):
                left = Node(freq = left[1], char = left[0])
            right = lst.pop()
            if not isinstance(right, Node):
                right = Node(freq = right[1], char = right[0])
            new_node = Node(right.freq + left.freq)
            new_node.right = right
            new_node.left = left
            lst.append(new_node)
            lst.sort(key=lambda x: x[1] if not isinstance(x, Node) else x.freq, reverse=True)
        return FrequencyTree(lst[0])

def get_character_count(string):
    chars = {}
    for char in string:
        chars[char] = chars.get(char, 0) + 1
    return chars

if __name__ == "__main__":
    main()
