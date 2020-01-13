from Hangman import Hangman
from getpass import getpass
word = getpass("Enter Word Here -> ")
game = Hangman(word)
print("Game has started:\n\n")
print(game.getWord() + "\n\n")
letter = input("Enter a letter (enter only one letter) -> ")
again = True

while len(letter) <= 1 and again:
    signal  = game.guess(letter)
    print(signal)
    if signal == game.LOSE:
        break
    else:
        if not game.getWord().__contains__("_"):
            print(game.WIN)
            break
        else:
            letter = input("Enter a letter (enter only one letter) -> ")