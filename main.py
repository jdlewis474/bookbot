def get_book():
    book_path = str(input("Please input file path to book: \n"))
    with open(book_path) as book:
        book_txt = book.read()
        return book_txt

def print_book(text):
    print(text)
    return

def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_split(text):
    nested_chars = []
    nested_chars.append(list(text))
    chars = []
    for word in nested_chars:
        for char in word:
            chars.append(char.lower())
    return chars

def char_count(chars):
    import string
    alphabet = list(string.ascii_lowercase)
    count_dict = dict.fromkeys(alphabet, 0)
    for char in chars:
        for letter in count_dict:
            if char == letter:
                count_dict[letter] += 1
    return count_dict

def main():
    booktext = get_book()
    char_list = char_split(booktext)
    num_words = word_count(booktext)
    char_dict = char_count(char_list)
    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words," words found in the document")
    for char_key in char_dict:
        print("the ",char_key," character was found ",char_dict[char_key], "times")

main()