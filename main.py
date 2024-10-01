def get_book():
    with open("books/frankenstein.txt") as frank_book:
        frank_txt = frank_book.read()
        return frank_txt

def print_book(text):
    print(text)
    return

def word_count(text):
    word_list = text.split()
    return len(word_list)


def main():
    booktext = get_book()
    print(word_count(booktext))
    


main()