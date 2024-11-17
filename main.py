def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # wordcount = number_of_words(text)
    # print(wordcount)
    # print(character_count(text))
    # sort_list(character_count(text))
    create_report(book_path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def number_of_words(text):
    return len(text.split())

def character_count(text):
    char_count = {}
    lower_case = text.lower()
    for c in lower_case:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] +=1
    return char_count

def sort_on(d):
    return d["num"]

def sort_list(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def create_report(book_path, text):
    sorted_list = sort_list(character_count(text))
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words(text)} words found in the document")
    print()
    for i in sorted_list:
        print(f"The {i['char']} character was found {i['num']} times")
    # print(sort_list(character_count(text)))
    print("--- End report ---")


main()