from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, direction):
    match direction:
        case 'encode':
            pass
        case 'decode':
            shift_amount *= -1
        case _:
            print('Invalid direction')

    end_text = ""
    for char in start_text:
        if char in alphabet:
            end_text += alphabet[(alphabet.index(char) +
                                  shift_amount) % len(alphabet)]
        else:
            end_text += char
    print(f'The {direction}d text is {end_text}')


if __name__ == '__main__':
    print(logo)
    should_continue = True
    while(should_continue):
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text, shift, direction)

        choice = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

        match choice:
            case 'yes':
                should_continue = True
            case 'no':
                should_continue = False
            case _:
                should_continue = False
