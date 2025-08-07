import sys

from stats import get_word_count, get_character_count, sorted_character_count

def get_book_text(filepath):
    """
    Reads the content of a book from a given file path.
    
    :param filepath: Path to the book file
    :return: Content of the book as a string
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "The specified book file does not exist."
    except Exception as e:
        return f"An error occurred while reading the book: {e}"



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # filepath = 'books/frankenstein.txt'
    filepath = sys.argv[1]
    print(f"Filepath: {filepath}")
    book_text = get_book_text(filepath)
    num_words = get_word_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    num_characters = get_character_count(book_text)
    sorted = sorted_character_count(num_characters)

    for pair in sorted:
        print(f"{pair["char"]}: {pair["num"]}")

if __name__ == "__main__":
    main()# main.py