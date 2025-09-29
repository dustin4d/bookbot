def word_count(book_text):
    splitted = book_text.split()
    num_words = 0
    for word in splitted:
        num_words += 1

    return f"Found {num_words} total words"

def char_count(book_text):
    char_obj = {}

    # add each unique value (lowercased) to the object
    for char in book_text:
        c = char.lower()
        if not c in char_obj:
            char_obj[c] = 0
        char_obj[c] += 1

    return char_obj

# helper fn, use inside `sort_char_counts`
# `item` will be ?
def sort_on(item):
    return item["num"]

def sort_char_counts(dict_of_chars):
# take in the dict(obj) of the characters and their counts
# return the sorted list of dicts 
    list_of_dicts = [] # <character>:<count>

    # iterate through the dataset, separate the key/val pairs
    for char, num in dict_of_chars.items():
        # create a new dict with `char` and `num` for each iteration
        list_of_dicts.append({"char": char, "num": num})
    
    # show the highest number first (reverse true), and run through sort helper fn
    list_of_dicts.sort(reverse=True, key=sort_on)

    # print out the data in required format
    # use i in range, we need each index
    for i in range(0, len(list_of_dicts)):
        char_dict = list_of_dicts[i] # save each dict to a var
        print(f"{char_dict["char"]}: {char_dict["num"]}") # pull the data from each dict

# test doesn't require a return value, only expects printed values from above :P