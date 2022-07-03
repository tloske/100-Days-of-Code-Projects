# Password Generator Project
import random
from multiprocessing import Process, Queue
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


def easy(nr_letters, nr_symbols, nr_numbers, q):
    password = []
    q_easy = Queue()
    p_letters = Process(target=get_symbol_list,
                        args=(nr_letters, letters, q_easy,))
    p_symbols = Process(target=get_symbol_list,
                        args=(nr_symbols, symbols, q_easy,))
    p_numbers = Process(target=get_symbol_list,
                        args=(nr_numbers, numbers, q_easy,))
    p_letters.start()
    p_symbols.start()
    p_numbers.start()
    password.extend(q_easy.get())
    password.extend(q_easy.get())
    password.extend(q_easy.get())
    p_letters.join()
    p_symbols.join()
    p_numbers.join()
    q.put("Easy: {password}".format(password="".join(password)))


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def hard(nr_letters, nr_symbols, nr_numbers, q):
    password = []
    q_hard = Queue()
    p_letters = Process(target=get_symbol_list,
                        args=(nr_letters, letters, q_hard,))
    p_symbols = Process(target=get_symbol_list,
                        args=(nr_symbols, symbols, q_hard,))
    p_numbers = Process(target=get_symbol_list,
                        args=(nr_numbers, numbers, q_hard,))
    p_letters.start()
    p_symbols.start()
    p_numbers.start()
    password.extend(q_hard.get())
    password.extend(q_hard.get())
    password.extend(q_hard.get())
    p_letters.join()
    p_symbols.join()
    p_numbers.join()
    random.shuffle(password)
    q.put("Hard: {password}".format(password="".join(password)))


def get_symbol_list(amount, list, q):
    q.put([random.choice(list) for x in range(amount)])


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    start = time.time()
    q = Queue()
    p_easy = Process(target=easy, args=(
        nr_letters, nr_symbols, nr_numbers, q,))
    p_hard = Process(target=hard, args=(
        nr_letters, nr_symbols, nr_numbers, q,))
    p_easy.start()
    p_hard.start()
    print(q.get())
    print(q.get())
    p_easy.join()
    p_hard.join()
    end = time.time()
    print(end - start)
