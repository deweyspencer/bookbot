def get_num_words(booktext):
    return len(booktext.split())

def get_character_count(booktext):
    char_counter = {}
    for char in booktext:
        char = char.lower()
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter

def sort_on (entry):
    return entry["num"]

def get_sorted_list(char_count_dict):
    the_list = []
    for key, value in char_count_dict.items():
        if key[0].isalpha():
            the_list.append({"char": key, "num": value})
    #print(the_list.sort(key=lambda x: x["num"]))
    the_list.sort(reverse=True,key=sort_on)
    return the_list
