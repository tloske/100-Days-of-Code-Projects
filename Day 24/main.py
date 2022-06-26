# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def get_letter():
    with open('Input/Letters/starting_letter.txt') as file:
        letter = file.read()

    return letter


def get_names():
    with open('Input/Names/invited_names.txt') as file:
        names = [name.rstrip() for name in file.readlines()]

    return names


if __name__ == '__main__':

    letter = get_letter()
    names = get_names()

    for name in names:
        with open(f'Output/ReadyToSend/{name}.txt', 'w') as file:
            file.write(letter.replace('[name]', name))
