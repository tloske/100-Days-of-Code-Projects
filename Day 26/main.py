import pandas


def get_phonetic_alphabet():
    return {letter: word for (letter, word) in pandas.read_csv(
        'nato_phonetic_alphabet.csv').itertuples(index=False)}


def create_phonetic_list(word, phonetic_alphabet):
    return [phonetic_alphabet[letter] for letter in word]


def main():
    phonetic_alphabet = get_phonetic_alphabet()

    word = input("Type in a word: ").upper()

    try:
        print(create_phonetic_list(word, phonetic_alphabet))
    except KeyError:
        print("Sorry, only letters int the alphabet.")
        main()


if __name__ == '__main__':
    main()
