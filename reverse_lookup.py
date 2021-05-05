##
# reverse_lookup.py
# Finds all the keys that map to a value. The function will take the
# dictionary and the value to search as parameters


def key_mashing(dictionary):
    """
    Converts repeated keys' values in a .item() to a list.
    """
    if type(dictionary) == dict:
        dictionary = invert_dict(dictionary)

    mashed_dictionary = {}

    for item in dictionary:
        key, value = item

        # Check if the item is already in the dict
        if key not in mashed_dictionary:
            # Add to the dictionary
            mashed_dictionary[key] = value

        # Append to the relevant value
        elif type(mashed_dictionary[key]) == list:
            mashed_dictionary[key].append(value)

        # If two keys are the same then convert the values into a list
        else:
            mashed_dictionary[key] = [mashed_dictionary[key], value]

    return mashed_dictionary


def invert_dict(dictionary):
    """
    Returns a list of tuples equivalent to key and value.
    These are the same as the dictionary except reverse
    {key: value} -> [(value, key)]
    """
    inverted_items = []

    # Invert em into a new list
    for item in dictionary.items():
        inverted_items.append((item[1], item[0]))

    return inverted_items



def reverse_lookup(dictionary, value):
    """
    Reverse lookup by value
    """
    reverse_dictionary = key_mashing(dictionary)

    try:
        return reverse_dictionary[value]

    except:
        print("Value not in dictionary!")


if __name__ == "__main__":
    # Sample dictionary
    languages = {
            "NZ":           "English",
            "Australia":    "English",
            "Spain":        "Spanish",
            "Brazil":       "Portuguese",
            "Chile":        "Spanish"
            }

    val = input("Value to search for: ")

    print(reverse_lookup(languages, val))
