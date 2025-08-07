def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in
    :return: Number of words in the text
    """
    return len(text.split())

def get_character_count(text):
    """
    Counts the number of characters in a given text.
    
    :param text: The text to count characters in
    :return: The number of times each character, (including symbols and spaces), appears in the string.
    """

    new_dict = {}

    for char in text:
        char = char.lower()
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    

    return new_dict


def sort_on(items):
    """
    Sort by nun
    """
    return items["num"]


def sorted_character_count(dict):
    """
{'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7630, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}

    """
    new_list = []

    for key in dict:
        new_list.append({"char": key, "num": dict[key]})

    new_list.sort(reverse=True, key=sort_on)

    return new_list


