# Wordle Solver created by Alex Tomsovic
# linktr.ee/alextomsovic

import datetime

space =  " "
word_list = []
with open("wordle_answer_list.txt") as file:
    for line in file:
        word_list.append(line.strip())

def start_wordle(word_list : list) -> None:
    """Remove incorrect words"""
    while len(word_list) > 1:
        word_index = []
        for position in range(5):
            letter = input("Letter entered into positon " + str(position+1) +"?: ").lower()
            print(space)
            color = input("Color returned (G,Y,B)?: ").lower() # Black - Yellow - Green
            print(space)
            if color != 'g' and color != 'y' and color != 'b':
                print("Color input invalid.")
                return 
            word_removal = []
            for word in word_list:
                if color == 'g':
                    if word[position] != letter:
                        word_removal.append(word)
                        if letter not in word_index:
                            word_index.append(letter)
                elif color == 'y':
                    if letter not in word:
                        word_removal.append(word)
                    elif word[position] == letter:
                        word_removal.append(word)
                    if letter not in word_index:
                        word_index.append(letter)
                elif color == 'b':
                    if letter in word:
                        if letter not in word_index:
                            word_removal.append(word)
                        elif word_list[position] == letter:
                            word_removal.append(word)
            for word in word_removal:
                word_list.remove(word)
        print(word_list)
        print(space)
        guess = input("Was your guess correct (Y/N)?: ").lower()
        print(space)
        if guess == 'y':
            current_date = datetime.datetime.now()
            print(space)
            print("Congradulations on solving the " + current_date.strftime("%c") + " wordle!")
            print(space)
            return
start_wordle(word_list)
