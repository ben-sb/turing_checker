from itertools import product, chain

def check(tm, length = 4):
    words = ['']
    for i in range(1, length + 1):
        perms = product(tm.input_alphabet, repeat = i)
        words = chain(words, perms)

    accepted_words = []
    rejected_words = []

    for w in words:
        word = ''.join(w)
        char_list = list(w)
        if tm.run(char_list):
            accepted_words.append(word)
        else:
            rejected_words.append(word)

    print(f'\nAccepted {len(accepted_words)} words:')
    print(accepted_words)

    print(f'\nRejected {len(rejected_words)} words:')
    print(rejected_words)


