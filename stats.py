def count_words(text):
    words = text.split()
    return len(words)

def characters_count(text):
    text = text.lower()
    character_count = {}
    for c in text:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_characters_by_count(character_dict):
    result_list = []
    for key, value in character_dict.items():
        result_list.append({"char": key, "num": value})

    result_list.sort(key=sort_on, reverse=True)
    
    return result_list
