import random
import  csv
def file_len(file):
    for i, l in enumerate(file):
            pass
    return i + 1

def hangman(word):
    wrong = 0
    stages = ["",
              "_________       ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              '|       /|\     ',
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

words = []
with open('words.csv','r') as file:
    reader = csv.reader(file)
    for line in reader:
        words.append(line)

word = words[random.randrange(0,len(words),)]

print(word[0])
word[0] = word[0].replace(' ','')
print(word[0])