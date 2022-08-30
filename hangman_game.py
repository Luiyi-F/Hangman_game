from hangman_art import HANGMANPICS, END_MESSAGES, HANGMAN
import random
import os
import unidecode

def clear():
    os.system('clear')

def read():
    words = []
    with open("./data.txt", "r" , encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            words.append(line)
    return words

def exist_char(char, word, result):
    char_flag = False
    for i in range(len(word)):
        if(unidecode.unidecode(word[i].lower()) == char):
            result[i] = word[i]
            char_flag = True
    return char_flag

def main():
    clear()
    words = read()
    tries = 0
    word = words[random.randint(0, len(words))]
    split_word = list(word)
    result_word = list(map(lambda low: "_", split_word))

    while(result_word != split_word and tries < 6):
        print(HANGMAN)
        print(HANGMANPICS[tries])
        print(result_word)
        char = input("Ingrese una letra: ")
        try:
            if len(char) != 1 or char.isnumeric():
                raise ValueError("solo ingrese letras")
            if(not exist_char(unidecode.unidecode(char.lower()), split_word, result_word)):
                tries+=1
        except ValueError:
            print(ValueError)
        clear()

    if(tries < 6):
        print(END_MESSAGES[0])
    if(tries > 6):
        print(END_MESSAGES[1])

    print(HANGMANPICS[tries])
    print("La palabra es: "+ word)


if __name__ == '__main__':
    main()