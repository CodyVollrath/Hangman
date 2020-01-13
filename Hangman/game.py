from Hangman import Hangman
from getpass import getpass
word = getpass("Enter Word Here -> ")
game = Hangman(word)
print("Game has started:\n\n")
print(game.getWord() + "\n\n")
letter = input("Enter a letter (enter only one letter) -> ")

while len(letter) <= 1:
    signal  = game.guess(letter)
    print(signal)
    game.displayLettersTried()
    if signal == game.LOSE:
        print("Word was: " + game.word)
        break
    else:
        if not game.getWord().__contains__("_"):
            print(game.WIN)
            break
        else:
            letter = input("Enter a letter (enter only one letter) -> ")