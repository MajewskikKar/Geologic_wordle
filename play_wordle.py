from wordle import Wordle
from diction import check_word
import random
import pandas as pd

def rand_word():
    read_words = pd.read_excel('slowa.xlsx')
    words_list = read_words['6 liter'].values.tolist()
    secret_word = random.choice(words_list)
    return secret_word
def main():

    file = 'slowa.xlsx'
    secret = rand_word()
    wordle = Wordle(secret)


    print("Cześć graczu geologu")
    while wordle.can_atttempt:
        x = input("wpisz słowo:")

        if len(x) != wordle.WORD_LENGTH:
            print(f"słowo musi zawierać {wordle.WORD_LENGTH} znaków")
            continue
        if check_word(x) != True:
            print("słowo nie występuje w słowniku. Wpisz inne.")
            continue
        wordle.attempt(x)
        result = wordle.guess(x)
        print(f'Pozostało prób: {wordle.remaining_attempts}')
    if wordle.is_solved:
        print("gratulacje, zgadłeś")
    else:
        print(f"PRZEGRANA :(, hasłem było {secret}")
        print(f'https://sjp.pl/{secret}')
if __name__ == '__main__':
    main()