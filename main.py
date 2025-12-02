import sys
from stats import count_word_in_text
from stats import count_characters_in_text
from stats import dict_to_sort_list
def read_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents
def print_lines(from_list):
     for c in from_list:
        print(c["char"] + ":", c["num"])

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        #print(sys.argv[1])
        file_path = sys.argv[1]
    book_text = read_book_text(file_path)
    num_words = count_word_in_text(book_text)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = count_characters_in_text(book_text)
    print_lines(dict_to_sort_list(char_dict))
    print("============= END ===============")
main()