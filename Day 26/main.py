import pandas


def get_phonetic_alphabet():
    return {letter: word for (letter, word) in pandas.read_csv(
        'nato_phonetic_alphabet.csv').itertuples(index=False)}


def create_phonetic_list(word, phonetic_alphabet):
    return [phonetic_alphabet[letter] for letter in word]


if __name__ == '__main__':
    phonetic_alphabet = get_phonetic_alphabet()

    word = input("Type in a word: ").upper()

    print(create_phonetic_list(word, phonetic_alphabet))
