import argparse

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
    # get character frequency
    char_freq = get_character_count(data)

    fh.close()  
    return 0

def get_character_count(string):
    chars = {}
    for char in string:
        chars[char] = chars.get(char, 0) + 1
    return chars

if __name__ == "__main__":
    main()
