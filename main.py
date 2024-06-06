def book_string(path):
    with open(path) as book:
        return book.read()


def read_book(path):
    text = book_string(path)
    return text


def word_count(path):
    text = book_string(path)
    words = text.split()
    return len(words)


def num_chars(path):
    text = read_book(path)
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def report(path):
    print(f"Report on {path}\n\n")
    print(f"{word_count(path)} words were found in the book\n")
    unsorted_dict = num_chars(path)
    sorted_dict = chars_dict_to_sorted_list(unsorted_dict)
    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    book_path = "books/frankenstein.txt"
    report(book_path)


if __name__ == '__main__':
    main()
