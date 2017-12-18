def break_workds(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def printf_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_workds(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_workds(sentence)
    printf_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    printf_first_word(words)
    print_last_word(words)