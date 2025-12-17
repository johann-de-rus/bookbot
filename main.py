import sys
from stats import count_words, characters_count, sort_characters_by_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Usage: python3 main.py {file_path}")

    contents = get_book_text(file_path)
    characters_occurence = characters_count(contents)
    num_words = count_words(contents)
    print_reported_characters(
        sort_characters_by_count(characters_occurence),
        num_words
    )

def print_reported_characters(character_list, charachter_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {charachter_count} total words")
    print("--------- Character Count -------")
    for char in character_list:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()