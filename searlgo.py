
#text_search gets the first occurence of the pattern
def text_search(text, pattern):
    # if type(text) == str:
    # new = text.split()
    text_length = len(text)
    pattern_length = len(pattern)
    result = []

    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            result.append(i)
    return result
    
def search_list(strings, pattern):
    pattern = pattern.lower()  # To ensure case-insensitive search
    pattern_length = len(pattern)
    result = []

    for index, string in enumerate(strings):
        string_lower = string.lower()
        string_length = len(string_lower)

        # Naive search algorithm for the current string
        for i in range(string_length - pattern_length + 1):
            match = True
            for j in range(pattern_length):
                if string_lower[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(index)
                break  # Move to the next string in the list after the first match

    return result
    
def search_partial(strings, pattern):
    pattern = pattern.lower()  # To ensure case-insensitive search
    pattern_length = len(pattern)
    result = []

    for index, string in enumerate(strings):
        string_lower = string.lower()
        string_length = len(string_lower)

        # Naive search algorithm for the current string
        for i in range(string_length - pattern_length + 1):
            match = True
            for j in range(pattern_length):
                if string_lower[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append((string, index))
                break  # Move to the next string in the list after the first match
    return result
