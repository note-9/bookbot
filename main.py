import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_path):
    word_string = get_book_text(file_path)
    list = word_string.split()
    count = 0
    for i in list:
        count += 1
    return count

def char_freq(file_path):
    word_string = get_book_text(file_path).lower()
    dict = {}
    for i in word_string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


def sort_on(items):
    return items["num"]


def sorted_list_dict(dict):
    list = []
    for i in dict:
        a = {}
        a["char"] = i
        a["num"] = dict[i]
        list.append(a)
    list.sort(reverse=True, key=sort_on)
    return list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {file_path}...")
    print("-------- Word Count ---------")
    print(f" Found {get_num_words(file_path)} total words")
    print("------ Character Count ------")
    freq = char_freq(file_path)
    for i in sorted_list_dict(freq):
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    return 0

main()
