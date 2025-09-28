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

def sort_on(items):
    return items["num"]

def sorted(dict_of_chars):
# take in the dict(obj) of the characters and their counts
# return the sorted list of dicts 
    list_of_dicts = [] # <character>:<count>

    # iterate through char_obj and make a dict for each pair
    for key, value in dict_of_chars.items(): # get key/val pairs and not just keys
        list_of_dicts.append({key:value}) # append single dict for each iteration

    # use a helper function to provide a metric for the sort method to sort by number
    nums = sort_on(dict_of_chars)
    print(nums)

