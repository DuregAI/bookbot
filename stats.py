def count_word_in_text(text):
    words_count = len(text.split())
    return words_count
def count_characters_in_text(text):
    text = text.lower()
    char_list = dict ()
    for c in text:
        if c in char_list:
            char_list[c] += 1
        else:
            char_list[c] = 1
    return char_list
def sort_on(items):
    return items["num"]
def dict_to_list(dictionary):
    to_list = []
    for c in dictionary:
        if c.isalpha():
            to_list.append({"char" : c, "num" : dictionary[c]})
    return to_list
def dict_to_sort_list(dictionary):
    my_list = dict_to_list(dictionary)
    my_list.sort(reverse=True, key=sort_on)
    return my_list