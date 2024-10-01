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
    print(char_count(char_list))

main()