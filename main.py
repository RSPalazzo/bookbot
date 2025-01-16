def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        letters = count_letters(file_contents)
        list_of_letters = chars_dict_to_sorted_list(letters)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print("")
        for i in list_of_letters:
            if not i["name"].isalpha():
                continue
            print(f"The {i["name"]} character was found {i["num"]} times")
        print("--- End report ---")

def count_words(book):
    count = 0
    for i in book.split():
        count += 1
    return count

def count_letters(book):
    letter_counts = {}
    for word in book.split():
        for letter in word:
            letter_lower = letter.lower()
            if letter_lower in letter_counts:
                letter_counts[letter_lower] += 1
            else:
                letter_counts[letter_lower] = 1
    return letter_counts

def sort_on(final_dict):
    return final_dict["num"]

def chars_dict_to_sorted_list(letter_counts):
    letter_list = []
    for letter in letter_counts:
        letter_list.append({"name": letter, "num": letter_counts[letter]})
    letter_list.sort(reverse=True, key=sort_on)

    return letter_list

main()
